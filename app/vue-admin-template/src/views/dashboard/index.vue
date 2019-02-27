<template>
  <div class="app-container">
    <el-row :gutter="10">
      <el-col :span="5"><div class="grid-content bg-purple"/></el-col>
      <el-col :span="14">
        <el-table
          :data="tableData"
          style="width: 100%">
          <el-table-column
            prop="date"
            label="日期"
            width="180"/>
          <el-table-column
            prop="name"
            label="姓名"
            width="180"/>
          <el-table-column
            prop="address"
            label="地址"/>
      </el-table></el-col>
      <el-col :span="5"><div class="grid-content bg-purple"/></el-col>
    </el-row>
    <el-row :gutter="10">
      <el-col :span="4"><div class="grid-content bg-purple"/></el-col>
      <el-col :span="16"><div class="grid-content bg-purple"/></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"/></el-col>
    </el-row>

  </div>
</template>
<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
<script>
export default {
  data() {
    return {
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
  }
}
</script>
