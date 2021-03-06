#!/usr/bin/env python

from datetime import datetime

from django.conf import settings

from jss.models import Computer, Site, ComputerApplication
from jss.jss_api import JSSAPISession


casper_client = JSSAPISession(settings.JSS_URL, settings.JSS_USER, settings.JSS_PASSWORD)

def update_computer(jss_id, name):
    print('Syncing computer: {}'.format(name))
    request = casper_client.lookup_by_id(jss_id).json()
    
    jss_computer_details = request.get('computer')
    jss_computer_general = jss_computer_details.get('general')
    jss_computer_id = jss_computer_general.pop('id')
    
    jss_computer_purchasing = jss_computer_details.get('purchasing')
    jss_computer_hardware = jss_computer_details.get('hardware')
    jss_computer_info = dict()
    jss_computer_info.update(jss_computer_general)
    jss_computer_info.update(jss_computer_purchasing)
    jss_computer_info.update(jss_computer_hardware)


    jss_computer_location = jss_computer_details.get('location')
    jss_computer_info.update(jss_computer_general)
    jss_computer_info.update(jss_computer_location)


    jss_computer_software = jss_computer_details.get('software')
    jss_computer_applications = jss_computer_software.get('applications')

    field_names = [field.name for field in Computer._meta.get_fields()]
    for key, value in jss_computer_info.copy().items():
        if key not in field_names or value in ('', None):
            del jss_computer_info[key]
        elif 'utc' in key:
            jss_computer_info[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f%z')
     

    jss_site_details = jss_computer_info.pop('site')
    if jss_site_details:
        jss_site, _ = Site.objects.get_or_create(**jss_site_details)
    else:
        jss_site = None
    computer, _ = Computer.objects.get_or_create(computer_id=jss_computer_id, site=jss_site)
    for field, val in jss_computer_info.items():
        setattr(computer, field, val)
    computer.save()

    print('Syncing {} applications'.format(len(jss_computer_applications)))
    for application in jss_computer_applications:
        app, _ = ComputerApplication.objects.get_or_create(**application)
        computer.applications.add(app)
        computer.save()


def update_all_computers():
    request = casper_client.get_all_computers().json()
    for comp in request['computers']:
        update_computer(comp.get('id'), comp.get('name'))
