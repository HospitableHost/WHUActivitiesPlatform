<template>
  <div class="dashboard-container">
    <div class="dashboard-title">组织管理员信息：</div>
    <div class="dashboard-text">姓名: {{ name }}</div>
    <div class="dashboard-text">学号/工号: {{ schoolID }}</div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Cookies from 'js-cookie'
export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name',
      'schoolID'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.dashboard-title {
  color:#303133;
  font-size: 30px;
  margin-bottom: 20px;
}
.dashboard-text {
  color:#606266;
  font-size: 20px;
}
</style>
