import Cookies from 'js-cookie'

const TokenKey = 'vue_admin_template_token'
const SchoolIDKey = 'vue_admin_template_schoolID'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function getSchoolID() {
  return Cookies.get(SchoolIDKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function setSchoolID(schoolID) {
  return Cookies.set(SchoolIDKey, schoolID)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function removeSchoolID() {
  return Cookies.remove(SchoolIDKey)
}
