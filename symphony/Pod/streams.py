#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint streams methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


def member_add(self, stream_id, userid):
    ''' add a user to a stream '''
    req_hook = 'pod/v1/room/' + str(stream_id) + '/membership/add'
    req_args = '{ "id": %s }' % userid
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def member_remove(self, stream_id, userid):
    ''' remove user from stream '''
    req_hook = 'pod/v1/room/' + str(stream_id) + '/membership/remove'
    req_args = '{ "id": %s }' % userid
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def create_stream(self):
    ''' create a stream '''
    req_hook = 'pod/v1/im/create'
    req_args = None
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def create_stream_ni(self, userids):
    ''' create a stream in a non-inclusive manner '''
    req_hook = 'pod/v1/admin/im/create'
    req_args = json.dumps(userids)
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def create_room(self, room_definition):
    ''' create's a room '''
    req_hook = 'pod/v2/room/create'
    req_args = json.dumps(room_definition)
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def update_room(self, stream_id, room_definition):
    ''' update a room definition '''
    req_hook = 'pod/v2/room/' + str(stream_id) + '/update'
    req_args = json.dumps(room_definition)
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def room_info(self, stream_id):
    ''' get info on room '''
    req_hook = 'pod/v2/room/' + str(stream_id) + '/info'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return status_code, response


def activate_stream(self, stream_id, status):
    ''' de/reactivate a stream '''
    req_hook = 'pod/v1/room/' + str(stream_id) + '/setActive?active=' + self.__rest__.bool2str(status)
    req_args = None
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def room_members(self, stream_id):
    ''' get list of room members '''
    req_hook = 'pod/v2/room/' + str(stream_id) + '/membership/list'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return status_code, response
