<template >
  <div class="bgc">
    <!-- <canvas height="800" width="800" id="canva"></canvas> -->

    <div
      id="demo"
      style="position:absolute; width:100px; height:100px; background:#ccc; left:0; top:0;"
    ></div>
    <div class="div_class">
      <div>
        <el-input v-model="username" placeholder="用户名" :maxlength="30"></el-input>
        <el-input v-model="password" placeholder="密码" show-password></el-input>
      </div>
      <div class="button_class">
        <el-button type="primary" class="left" @click="Login()">登录</el-button>
        <el-button type="success" class="right" @click="register()">注册</el-button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Login",
  data() {
    return {
      password: "",
      username: "",
      filename: "",
      status: ""
    };
  },
  methods: {
    confirm() {
      if (this.password == "" || this.username == "") {
        this.$alert("密码、用户名不能为空", "FBI warning", {
          confirmButtonText: "确定",
          callback: action => {}
        });
      } else {
        this.$axios
          .post("/login_or_register", {
            pwd: this.password,
            usn: this.username,
            status: this.status
          })
          .then(response => {
            let data = response["data"];
            const status = data[0].status;
            const mes = data[0].result;
            // console.log(response);
            console.log(data[0].status);
            if (status == 1 || status == 4) {
              this.$alert(mes, "FBI warning", {
                confirmButtonText: "确定",
                callback: action => {}
              });
            }
            else{
              this.$router.push({
                path:'/homepage',
              })
            }
          })
          .catch(err => {});
      }
    },
    Login() {
      this.status = 1;
      this.confirm();
    },
    register() {
      this.status = 0;
      this.confirm();
    }
  },
  mounted() {}
};
</script>
<style lang="less">
.bgc {
  background-color: blanchedalmond;
  height: 100vh;
  width: 100vw;
  position: relative;
}
.div_class {
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  height: 20%;
  width: 20%;
  background-color: azure;
  padding: 100px 150px;
}
.button_class {
  width: 100%;
}
.left {
  float: left;
  width: 49%;
}
.right {
  float: right;
  width: 49%;
}
.el-button + .el-button {
  margin-left: 0px;
}
canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>