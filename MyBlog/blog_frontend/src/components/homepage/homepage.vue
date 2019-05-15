<template>
  <el-container>
    <el-aside width="40vh" style="height:100vh ; background-color:#545c64 ">
      <!-- Aside content -->
      <lm></lm>
    </el-aside>
    <el-container>
      <el-header height>
        <!-- Header content -->
        <el-row>
          <el-col :span="24">
            <div class="grid-content bg-purple-dark">wdf</div>
          </el-col>
        </el-row>
      </el-header>
      <el-main height>
        <!-- Main content -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
  <!-- <router-link to="Test"><h1>{{ msg }}</h1></router-link> -->
</template>

<script>
import lg from "@/components/homepage/context";
import lm from "@/components/homepage/Menu";
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
