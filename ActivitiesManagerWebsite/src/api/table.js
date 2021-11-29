import request from '@/utils/request'

export function getMyActivities(params) {
  return request({
    url: '/activity_op',
    method: 'get',
    params
  })
}

export function deleteActivity(params) {
  return request({
    url: '/activity_op',
    method: 'delete',
    params
  })
}

export function getOneActivity(params) {
  return request({
    url: '/oneActivity',
    method: 'get',
    params
  })
}