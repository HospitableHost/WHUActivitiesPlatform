
<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px" :rules="rules">
      <el-form-item label="活动名称"  prop='activity_title'>
        <el-col :span="12">
          <el-input v-model="form.activity_title" placeholder="活动名称" />
        </el-col>
      </el-form-item>
      <el-form-item label="发布组织" prop='organization_name'>
        <el-col :span="12">
          <el-input v-model="form.organization_name" placeholder="发布组织"/>
        </el-col>
      </el-form-item>
      <el-form-item label="面向院系" prop='oriented_department'>
        <el-select v-model="form.oriented_department" placeholder="面向院系">
          <el-option v-for="department in oriented_department" :label="department" :value="department" :key="department" />
        </el-select>
      </el-form-item>
      <el-form-item label="报名截止时间" prop='parti_ddl'>
        <el-col :span="10">
          <el-date-picker v-model="form.parti_ddl" type="datetime" placeholder="选择截止时间"  style="width: 100%;" />
        </el-col>
      </el-form-item>
      <!-- <el-form-item label="Instant delivery">
        <el-switch v-model="form.delivery" />
      </el-form-item> -->
      <el-form-item label="活动类型" prop='activity_type'>
        <el-radio-group v-model="form.activity_type">
          <el-radio label="文体竞赛" name="type" />
          <el-radio label="学科竞赛" name="type" />
          <el-radio label="讲座" name="type" />
          <el-radio label="趣味游戏" name="type" />
          <el-radio label="交友活动" name="type" />
          <el-radio label="文艺表演" name="type" />
          <el-radio label="社团招新" name="type" />
          <el-radio label="志愿活动" name="type" />
        </el-radio-group>
      </el-form-item>
      <!-- <el-form-item label="Resources">
        <el-radio-group v-model="form.resource">
          <el-radio label="Sponsor" />
          <el-radio label="Venue" />
        </el-radio-group>
      </el-form-item> -->


      <!-- :headers="{token:$cookieStorage.token}" -->
          <!-- :show-file-list="true" -->
          


      <el-form-item label="活动海报">
        <el-upload
          action="http://121.89.244.221:8000/activity_pic"
          ref="upload"
          :accept="'image/*'"
          :limit="1"
          :auto-upload="false"
          :on-exceed="handleExceed"
          :before-upload="handleBeforeUpload"
          :on-error="handleError"
          :on-progress="handleProgress"
          :on-success="handleSuccess">
          <el-button slot="trigger" size="small" type="primary">选取</el-button>
          <el-button style="margin-left: 10px;" type="success" size="small" @click="submitUpload">上传</el-button>
          <div slot="tip" class="el-upload__tip">请上传图片格式文件</div>
        </el-upload>
      </el-form-item>
      <el-form-item label="活动详情" prop="activity_detail">
        <el-input v-model="form.activity_detail" type="textarea" :rows='10' />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">发布</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { newActivity } from '@/api/newActivity'
export default {
  data() {
    return {
      form: {
        user_id: this.$store.getters.token,
        organization_name: '',
        oriented_department: '',
        activity_title: '',
        parti_ddl: null,
        publish_time: '',
        activity_type: '',
        activity_detail: '',
        activity_post: ''
      },
      oriented_department: ['全校','哲学学院','国学院','文学院','外国语言文学学院','新闻与传播学院','艺术学院(艺术教育中心)',
      '历史学院','经济与管理学院','法学院','马克思主义学院','社会学院','政治与公共管理学院','教育科学研究院','信息管理学院',
      '数学与统计学院','物理科学与技术学院','化学与分子科学学院','生命科学学院','资源与环境科学学院','高等研究院','动力与机械学院',
      '电气与自动化学院','城市设计学院','土木建筑工程学院','水利水电学院','工业科学研究院','电子信息学院','计算机学院','测绘学院',
      '遥感信息工程学院','印刷与包装系','网络安全学院','医学研究院','基础医学院','公共卫生学院','药学院','护理学院','第二临床学院',
      '口腔医学院','弘毅学堂','微电子学院'],
      files: [],
      rules:{
        activity_title :[{required: true, message: '请输入活动标题', trigger: 'blur'}],
        organization_name :[{required: true, message: '请输入发布组织', trigger: 'blur'}],
        oriented_department :[{required: true, message: '请选择面向院系', trigger: 'blur'}],
        parti_ddl :[{required: true, message: '请选择截止时间', trigger: 'blur'}],
        activity_type :[{required: true, message: '请选择活动类型', trigger: 'blur'}],
        activity_detail :[{required: true, message: '请输入活动详情', trigger: 'blur'}]
      },
      loading: false,
    }
  },
  methods: {
    onSubmit() {
      this.form.publish_time = new Date()
      this.$refs.form.validate(valid => {
        if (valid && this.form.publish_time<this.form.parti_ddl) {
          this.form.publish_time=this.form.publish_time.toISOString().split('.')[0]
          this.form.parti_ddl=new Date(this.form.parti_ddl).toISOString().split('.')[0]
          this.loading = true
          // console.log(JSON.stringify(this.form))
          newActivity(this.form).then(() => {
            this.$message({
            message: '发布成功！',
            type: 'success'
            });
            this.loading = false
            this.$refs.form.resetFields()
          }).catch((error) => {
            this.loading = false
          })
        } else if(valid){
          this.$message.error('截止日期必须晚于现在！');
          return false
        } else{
          this.$message.error('必须填完所有必填项！');
          return false
        }
      })

    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleExceed(){
      this.$message.error('只能上传一个文件，若需要更改，请删除原文件');
    },
    handleSuccess(response, file, fileList) {
      this.form.activity_post=response.url;
      this.$message({
        message: '上传成功',
        type: 'success'
      });
    },
    handleError() {
      this.$error("上传失败,请重新上传图片!");
    },
    handleBeforeUpload(file) {
      const isImage = file.type.includes("image");
      if (!isImage) {
        this.$message.error("上传文件类型必须是图片!");
        return false;
      }
      const isLt2M = file.size / 1024 / 1024 < 5;
      if (!isLt2M) {
        this.$message.error("上传图片大小不能超过 5MB!");
        return false;
      }
      return true;
    },
    handleProgress(event, file, fileList) {
      this.loading = true;  //  上传时执行loading事件
    }
  }
}
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

