import request from '@/utils/request'

export function newActivity(data) {
  return request({
    url: '/activity_new',
    method: 'post',
    data
  })
}