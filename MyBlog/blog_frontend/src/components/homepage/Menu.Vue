<template>
<div class="menucolor">
  <el-menu text-color="#fff"  mode="horizontal" class="menucolor" style="text-align: center;" :default-active="activeIndex" @select="handleSelect" router>
    <el-menu-item index="/">首 页</el-menu-item>
    <el-menu-item index ="/live">生 活</el-menu-item>
    <el-menu-item index = "/programm">编 程</el-menu-item>
  </el-menu>
  <!--:default-active当前激活菜单的 index   -->

  </div>
</template>
<script>
export default {
  name:'Menu',
  data() {
    return {
      activeIndex:{
        type:String,
        required:true,
      },
    }
  },
  methods: {
    // handleOpen(key, keyPath) {
    //   console.log(key, keyPath);
    // },
    // handleClose(key, keyPath) {
    //   console.log(key, keyPath);
    // },
    handleSelect(key,keyPath){

      // this.$router.push({path:'/context/'+key,})
    }
  }
};
</script>
<style lang='less'>
.menucolor{
  background-color: cadetblue;
}

.el-menu-item{
  font-size: 30px;
}
.el-menu--horizontal>.el-menu-item:not(.is-disabled):hover, .el-menu--horizontal>.el-submenu .el-submenu__title:hover {
  background-color:rgb(75, 154, 158);
}
.el-menu--horizontal>.el-menu-item:not(.is-disabled):focus, .el-menu--horizontal>.el-menu-item:not(.is-disabled):hover, .el-menu--horizontal>.el-submenu .el-submenu__title:hover {
    /* background-color: #fff; */
    background-color:rgb(75, 154, 158);
}
.el-menu--horizontal .el-menu-item:not(.is-disabled):focus, .el-menu--horizontal .el-menu-item:not(.is-disabled):hover {
    /* color: #303133; */
    color:beige;
}
.el-menu--horizontal>.el-menu-item.is-active {
    border-bottom: 2px solid #409EFF;
    color:beige;
}
</style>
