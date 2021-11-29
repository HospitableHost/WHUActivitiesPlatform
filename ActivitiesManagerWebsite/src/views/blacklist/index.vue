<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="blacklist"
      element-loading-text="加载中"
      border
      fit
      highlight-current-row
      height="630"
    >
      <el-table-column align="center" label="序号" width="70" :resizable="false">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="被拉黑用户昵称" width="220" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.user_nickname }}
        </template>
      </el-table-column>
      <el-table-column label="被拉黑用户姓名" width="200" align="center" :resizable="false">
        <template slot-scope="scope">
          <span>{{ scope.row.user_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="被拉黑用户学号/工号" width="180" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.school_id }}
        </template>
      </el-table-column>
      <el-table-column label="被拉黑用户所属学院/部门" width="220" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.department }}
        </template>
      </el-table-column>
      <el-table-column align="center" prop="banned_at" label="被拉黑时间" width="200" :resizable="false">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.banned_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="当时参与的活动" width="250" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.activity_title }}
        </template>
      </el-table-column>
      <el-table-column label="活动类型" width="100" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.activity_type }}
        </template>
      </el-table-column>
      <el-table-column label="活动管理者" width="200" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.organization_name }}
        </template>
      </el-table-column>
      <el-table-column label="事件描述" width="300" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.description }}
        </template>
      </el-table-column>      
      <el-table-column
        label="操作"
        width="125"
        align="center"
        fixed="right"
        :resizable="false">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="cancel(scope.$index)"
            type="primary"
            size="small"
            icon='el-icon-delete'
            :resizable="false"
            round>
            解除拉黑
          </el-button>
        </template> 
      </el-table-column>
      <div slot="empty" style="height:200px;line-height: 200px;text-align: left;font-size:30px;">
      <i class="el-icon-warning-outline"></i>暂无被拉黑用户
      </div>
    </el-table>
  </div>
</template>

<script>
import { getBlacklist, cancelBan, newBan } from '@/api/blacklist'
import Vue from 'vue'
export default {
  data() {
    return {
      blacklist: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getBlacklist({admin_userid:this.$store.getters.token}).then(response => {
        this.blacklist = response.data
        for(let i=0; i<this.blacklist.length; i++){
          const bannedDate = new Date(this.blacklist[i].banned_time+'+00:00')
          this.blacklist[i].banned_time=bannedDate.toLocaleString()
        }
        this.listLoading = false
      })
    },
    cancel(index)
    {
      cancelBan({admin_userid:this.$store.getters.token,banned_user_id:this.blacklist[index].banned_user_id}).then(response=>{
        Vue.delete(this.blacklist,index)
        this.$message({
          message:"解除成功",
          type:'success'
        })
      })
    }
  }
}
</script>
