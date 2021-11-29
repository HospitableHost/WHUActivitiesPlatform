
const tokens = {
  admin: {
    token: 'admin-token'
  },
  editor: {
    token: 'editor-token'
  }
}

const users = {
  'admin-token': {
    roles: ['admin'],
    introduction: 'I am a super administrator',
    avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    name: '党自强'
  },
  'editor-token': {
    roles: ['editor'],
    introduction: 'I am an editor',
    avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    name: 'Normal Editor'
  }
}

module.exports = [
  // user login
  {
    url: '/adminuser/login/',
    type: 'post',
    response: config => {
      const { username, password } = config.body
      // const token = tokens[username]
      // // mock error
      // if (!token) {
      //   return {
      //     code: 60204,
      //     message: 'Account and password are incorrect.'
      //   }
      // }

      // return {
      //   code: 1000,
      //   data: token
      // }
      if (username=="2018302110264") {
        if(password=="whuadmin"){
          return {
            code:1000,
            message:"登录成功",
            token:'1'
          }
        }
        else{
          return {
            code:1001,
            message:"密码错误",
          }
        }
      }
      else{
        return {
          code:1002,
          message:"该组织管理员不存在",
        }
      }

    }
  },

  // get user info
  {
    url: '/adminuser/info\.*',
    type: 'get',
    response: config => {
      const { token } = config.query
      // const info = users[token]
      const info = {
        roles: ['admin'],
        introduction: 'I am a super administrator',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: '党自强'
      }

      // mock error
      if (!info) {
        return {
          code: 50008,
          message: 'Login failed, unable to get user details.'
        }
      }

      return {
        code: 1000,
        data: info
      }
    }
  },

  // user logout
  {
    url: '/adminuser/logout',
    type: 'post',
    response: _ => {
      return {
        code: 1000,
        data: 'success'
      }
    }
  },
  {
    url: '/activity/picture/new',
    type: 'post',
    response: _ => {
      return {
        code: 1000,
        message: 'success',
        url: 'http://dzq'
      }
    }
  },
  {
    url: '/activity_new',
    type: 'post',
    response: _ => {
      return {
        code: 1000,
        message: '发布成功',
        url: 'http://dzq'
      }
    }
  }  
]
