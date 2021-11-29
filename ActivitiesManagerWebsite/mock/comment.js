const comment = {
    data: [
      {
        comment_id: '1', //评论主键id
        comment_time: '2021-11-21T13:10:00+08:00',  //评论时间
        activity_id: '10', //活动的id
        user_id: 'errhefe232213',  //评论者id
        user_nickname: '犀利的评论家',   //评论者昵称
        user_avatar: 'http://ww4.sinaimg.cn/bmiddle/006DLFVFgy1ft0j2pddjuj30v90uvagf.jpg', //评论者头像url
        comment_content: '非常靠谱的程序员',  //评论内容
        reply: [  //回复，即子评论
          {
            from_comment_id: '2',  //该评论的主键
            comment_time: '2021-11-21T13:10:00+08:00',   //评论时间
            activity_id: '10',
            user_id: 'observer223432',  //评论者id
            user_nickname: '夕阳红',  //评论者昵称
            comment_content: '赞同，很靠谱，水平很高',  //评论内容
            to_user_nickname: '犀利的评论家',  //被评论者昵称
            to_comment_id: '1'  
                  
          },
          {
            from_comment_id: '3',
            comment_time: '2021-11-21T13:10:00+08:00',
            activity_id: '10',
            user_id: 'observer567422',
            user_nickname: '清晨一缕阳光',
            comment_content: '大神一个！',       
            to_user_nickname: '夕阳红',
            to_comment_id: '2'            
          }
        ]
      },
      {
        comment_id: '4',
        comment_time: '2021-11-21T13:10:00+08:00',
        activity_id: '10',
        user_id: 'errhefe232213',
        user_nickname: '毒蛇郭德纲',
        user_avatar: 'http://ww1.sinaimg.cn/bmiddle/006DLFVFgy1ft0j2q2p8pj30v90uzmzz.jpg',
        comment_content: '从没见过这么优秀的人',
        reply: []
      },
      {
        comment_id: '5',
        comment_time: '2021-11-21T13:10:00+08:00',
        activity_id: '10',
        user_id: 'errhefe232213',
        user_nickname: '毒蛇郭德纲',
        user_avatar: 'http://ww1.sinaimg.cn/bmiddle/006DLFVFgy1ft0j2q2p8pj30v90uzmzz.jpg',
        comment_content: '从没见过这么优秀的人',
        reply: []
      },
      {
        comment_id: '6',
        comment_time: '2021-11-21T13:10:00+08:00',
        activity_id: '10',
        user_id: 'errhefe232213',
        user_nickname: '毒蛇郭德纲',
        user_avatar: 'http://ww1.sinaimg.cn/bmiddle/006DLFVFgy1ft0j2q2p8pj30v90uzmzz.jpg',
        comment_content: '从没见过这么优秀的人',
        reply: []
      }
    ]
  };
  


module.exports = [
  {
    url: '/comments_act_all',
    type: 'get',
    response: config => {
        return {
          code: 1000,
          data: comment.data,
          message: '获取成功'
      }
    }
  },
  {
    url: '/comment',
    type: 'delete',
    response: config => {
        return {
          code: 1000,
          message: '删除成功'
      }
    }
  },
  {
    url: '/comment/new/toActivity',
    type: 'post',
    response: config => {
        return {
          code: 1000,
          message: '评论成功',
          commentInfo: {
            comment_id: '7',
            comment_time: '2021-11-21T13:10:00+08:00',
            activity_id: '10',
            user_id: 'errhefe232213',
            user_nickname: '毒蛇郭德纲',
            user_avatar: 'http://ww1.sinaimg.cn/bmiddle/006DLFVFgy1ft0j2q2p8pj30v90uzmzz.jpg',
            comment_content: '从没见过这么优秀的人'
          }
      }
    }
  },
  {
    url: '/comment/new/toComment',
    type: 'post',
    response: config => {
        return {
          code: 1000,
          message: '评论成功',
          commentInfo: {
            from_comment_id: '8',  //该评论的主键
            comment_time: '2021-11-21T13:10:00+08:00',   //评论时间
            activity_id: '10',
            user_id: 'observer223432',  //评论者id
            user_nickname: '夕阳红',  //评论者昵称
            comment_content: '赞同，很靠谱，水平很高',  //评论内容
            to_user_nickname: '犀利的评论家',  //被评论者昵称
            to_comment_id: '1'  
                  
          }
      }
    }
  }  

]
  