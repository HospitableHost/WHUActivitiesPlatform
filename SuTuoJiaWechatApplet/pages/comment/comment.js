const app = getApp()

// pages/comment/comment.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    currentTab:0,
    isShow:false,
    user_id:0,
    comments:{},
    reply_comments:{},
    replied_comments:{},
    reply:{},
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({  // GET数据中有json格式似乎可能出错
      url: app.globalData.base_path+'/comment_all?user_id='+app.globalData.user_id,
      method:'GET',
      data:{user_id: app.globalData.user_id},
      header:{"Content-Type":"application/json"},
      success: function(res){
        console.log(res.data);
        that.setData({ comments: res.data });
        that.setData({ reply_comments: res.data.commentToActivities })
        that.setData({ replied_comments: res.data.beReplied })
        that.setData({ reply: res.data.reply })
      },
      fail: function(){
        console.error("获取评论失败")
      },
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  tapTab: function (e) {
    console.log(e.currentTarget.dataset.ctab);
    let index = e.currentTarget.dataset.ctab
    this.setData({currentTab:index});
  },

  switchShow(){
    let that = this;
    this.setData({isShow:!that.data.isShow});
  },

  deleteComment() {
    wx.showModal({
      title: '提示',
      content: '确定要删除该评论吗？',
      success (res) {
        if (res.confirm) {
          console.log('用户点击确定')
          wx.request({
            url: app.globalData.base_path+'/comment_delete/',
            method:"DELETE",
            
          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },
})