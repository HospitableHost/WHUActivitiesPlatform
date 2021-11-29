const app = getApp()

// pages/user/user.js
Page({

  /**
   * 页面的初始数据
   */
  data:{
    name_value:"",
    sex_value:"",
    schoolid_value:"",
    grade_value:"",
    school_value:"",
    major_value:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  name:function(res){
    this.setData({
      name_value: res.detail.value//赋值给name_value
    })
  },

  sex:function(res){
    this.setData({
      sex_value: res.detail.value
    })
  },

  schoolid:function(res){
    this.setData({
      schoolid_value: res.detail.value
    })
  },

  grade:function(res){
    this.setData({
      grade_value: res.detail.value
    })
  },

  school:function(res){
    this.setData({
      school_value: res.detail.value
    })
  },

  major:function(res){
    this.setData({
      major_value: res.detail.value
    })
  },

  toComment() {
    wx.navigateTo({
      url: '../comment/comment'
    })
  },

  toMyActivity() {
    wx.navigateTo({
      url: '../myActivity/myActivity'
    })
  },
  data: {
   
    userInfo: null,  
    hidden:false,
    hiddenmodalput: true,
 
        //可以通过hidden是否掩藏弹出框的属性，来指定那个弹出框
  },
  modalinput: function () {
 
    this.setData({
 
      hiddenmodalput: !this.data.hiddenmodalput
 
    })
 
  },
 
  //取消按钮
 
  cancel: function () {
 
    this.setData({
 
      hiddenmodalput: true
 
    });
 
  },
 
  //确认
 
  confirm: function () {
    var that = this
    wx.request({
      url: app.globalData.base_path+'user_profile/',
      method: "POST",
      header: {
        "Content-Type": "application/json"
      },
      data:{
        user_id: app.globalData.user_id,
        password:"12345678",
      },

      success: function(res){
        console.log("提交成功")
      },
      fail: function(res){
        console.error("提交失败")
      }
    })

    this.setData({
 
      hiddenmodalput: true
 
    })
 
  },
  onChangeShowState: function () {
 
    var that = this;
 
    that.setData({
 
      showView: (!that.data.showView)
 
    })
 
  },
})