import request from '@/utils/request'

export function getParticipants(params) {
  return request({
    url: '/participants',
    method: 'get',
    params
  })
}

export function dealSignUp(data) {
  return request({
    url: '/signup',
    method: 'put',
    data
  })
}
