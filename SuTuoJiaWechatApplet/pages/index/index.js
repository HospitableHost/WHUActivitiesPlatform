const app = getApp()

Page({
  data: {
    index:0,
    openid:"",
    session_key:"",
    code:"",
    type:app.globalData.type,
    college:app.globalData.college,
    status:app.globalData.status,
    tIndex:0,
    cIndex:0,
    sIndex:0,
    ori_activities:[],
    activities:[],
    time:"",
  },

  onLoad() {
    var that = this

    wx.login({
      success: function (res) {
        app.globalData.CODE = res.code
        that.setData({
          code: res.code
        })
        
        wx.request({
          //获取openid接口  
          url: 'https://api.weixin.qq.com/sns/jscode2session',
          data: {
            appid: "wx6b4e5c68175ea327",
            secret: "88bc86e0a3ec96da0e435b52e90a2d1d",
            js_code: res.code,
            grant_type: 'authorization_code'
          },
          method: 'GET',
          success: function (res) {
            console.log(res.data)
            app.globalData.OPEN_ID = res.data.openid;//获取到的openid  
            app.globalData.SESSION_KEY = res.data.session_key;//获取到session_key  
            console.log(app.globalData.OPEN_ID.length)
            console.log(app.globalData.SESSION_KEY.length)
            that.setData({
              openid: res.data.openid.substr(0, 10) + '********' + res.data.openid.substr(res.data.openid.length - 8, res.data.openid.length),
              session_key: res.data.session_key.substr(0, 8) + '********' + res.data.session_key.substr(res.data.session_key.length - 6, res.data.session_key.length),
            })
          }
        })
      }
    })

    that.setData({
      activities: that.data.ori_activities
    })

    wx.request({
      url: app.globalData.base_path+'/activity_pt',
      method: 'GET',
      header: {"Content-Type":"application/json"}, 
      success: function(res){
        var Utils = require ( '../../utils/util.js' );
        console.log(res.data);
        var data = res.data.data;
        if (data.length > 0) {
          var allactivities = [];
          for (var i = 0; i < data.length; i++) {
            allactivities.push(data[i]);
            if(allactivities[i].partiddl >= Utils.formatTime(new Date())){
              allactivities[i].status = "正在报名"
            }
            else{
              allactivities[i].status = "报名截止"
            }
          }
          console.log(allactivities)
          that.setData({ ori_activities: allactivities });
          that.setData({ activities: allactivities });
        }

      },
      fail: function(){
        console.error("获取活动失败")
      },
  })
  },

  typeChange(e) {
    var that = this
    that.setData({
      tIndex: e.detail.value
    })
  },

  collegeChange(e) {
    var that = this
    that.setData({
      cIndex: e.detail.value
    })
  },
  statusChange(e) {
    var that = this
    that.setData({
      sIndex: e.detail.value
    })
  },

  filter_all: function(e){
    var that = this
    var allactivities = []
    var t_act = []
    var c_act = []
    var s_act = []
    for (var i = 0; i < that.data.ori_activities.length; i++) {
        if(that.data.tIndex != 0){
          if (that.data.ori_activities[i].activity_type == that.data.type[that.data.tIndex]){
            t_act.push(that.data.ori_activities[i])
          }
        }
        else{
          t_act.push(that.data.ori_activities[i])
        }
    }
    for (var i = 0; i < t_act.length; i++) {
      if(that.data.cIndex != 0){
        if (t_act[i].oriented_department == that.data.college[that.data.cIndex]){
          c_act.push(t_act[i])
        }
      }
      else{
        c_act.push(t_act[i])
      }
    }
    for (var i = 0; i < c_act.length; i++) {
      if(that.data.sIndex != 0){
        if (c_act[i].status == that.data.status[that.data.sIndex]){
          s_act.push(c_act[i])
        }
      }
      else{
        s_act.push(c_act[i])
      }
    }
    that.setData({
      activities: s_act
    })
  },

  toInfo: function(e) {
    let userid = e.currentTarget.dataset.userid
    let activityid = e.currentTarget.dataset.activityid
    let activitytitle = e.currentTarget.dataset.activitytitle
    let activitytype = e.currentTarget.dataset.activitytype
    let activitydetail = e.currentTarget.dataset.activitydetail
    let organizationname = e.currentTarget.dataset.organizationname
    let partiddl = e.currentTarget.dataset.partiddl
    let publishtime = e.currentTarget.dataset.publishtime
    let orienteddepartment = e.currentTarget.dataset.orienteddepartment
    let activitypost = e.currentTarget.dataset.activitypost
    let status = e.currentTarget.dataset.status
    wx.navigateTo({
      url: '../activity/activity?userid='+userid+'&activityid='+activityid+'&activitytitle='+activitytitle+'&activitytype='+activitytype+'&activitydetail='+activitydetail+'&organizationname='+organizationname+
      '&partiddl='+partiddl+'&publishtime='+publishtime+'&orienteddepartment='+orienteddepartment+'&status='+status+'&activitypost='+activitypost
    })
  },

  toApply: function(e){
    var that = this
    var Util = require( '../../utils/util.js' )
    //console.log("触发")
    console.log(e.currentTarget.dataset.status)
    if (app.globalData.user_id == -1) {
      wx.showToast({
        title: '还未完成认证！', 
        icon: 'error',  
        duration: 1500 
      })
    }
    
    else if (e.currentTarget.dataset.status == "报名截止"){
      wx.showToast({
        title: '活动报名已截止！', 
        icon: 'error',  
        duration: 1500 
      })
    }
    else{
      wx.showModal({
        title: '提示',
        content: '确定报名吗？',
        success (res) {
          if (res.confirm) {
            console.log('用户点击确定')
            wx.request({
              url: app.globalData.base_path+'/enrollment_participate/',
              method:'POST',
              header: {
                "Content-Type": "application/json"
              },
              data:{
                activity_id: e.currentTarget.dataset.activityid,
                user_id: app.globalData.user_id,
                parti_time: "2021-11-22T21:36:00",
              },
              success: function(res){
                wx.showToast({
                  title: '报名成功',
                  icon: 'success',
                  duration: 1500,
                })
              },
              fail: function(res){
                console.error("报名失败")
              }
            })

          } else if (res.cancel) {
            console.log('用户点击取消')
          }
        }
      })
    }
  }
})
