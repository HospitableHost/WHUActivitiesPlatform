import request from '@/utils/request'

export function getBlacklist(params) {
  return request({
    url: '/blacklist',
    method: 'get',
    params
  })
}

export function cancelBan(params) {
  return request({
    url: '/blacklist',
    method: 'delete',
    params
  })
}

export function newBan(data) {
  return request({
    url: '/blacklist',
    method: 'post',
    data
  })
}