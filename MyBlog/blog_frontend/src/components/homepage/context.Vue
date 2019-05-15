<template>
  <div class="card" id="card">
    <div class="br"></div>
    <el-row v-for="data in datalist" :key="data.id" @click.native="details(data.id)">
      <el-card :body-style="{ padding: '10px' }" shadow="hover">
        <div slot="header" class="header">
          <span>
            <!-- card title -->
            {{data.title}}
          </span>
        </div>
        <!-- card body -->
        <div class="comment">
          <!-- {{data.body}} -->
          我也不知道说啥好
        </div>
        <div class="br"></div>
        <div class="time">作者:{{data.author}} &nbsp &nbsp 发布时间:{{data.time}}</div>
      </el-card>
      <div class="br"></div>
    </el-row>
  </div>
</template>
<script>
export default {
  name: "Test",
  data() {
    return {
      datalist: []
    };
  },
  methods: {
    details(val) {
      const index = val % 7;

      this.$router.push({
        name: "details",
        query: {
          id: val + 1
        },
      });
    },
    // conn() {
    //   this.$axios
    //     .post("/add", {
    //     })
    //     .then(function(response) {
    //       console.log(response);

    //       console.log(response["data"][0]);
    //     })
    //     .catch();
    //   console.log(this.info.sex);
    // },
    query(val) {
      console.log(val + "query");
      this.$axios
        .post("/query", {
          type: val
        })
        .then(result => {
          this.datalist = [];
          console.log(result);
          let len = result["data"].length;
          // console.log(len);
          if (len != 0) {
            let obj = document.getElementById("card");
            obj.style.height = "";
            for (let index = 0; index < 7; index++) {
              this.datalist.push({
                title: result["data"][index].name,
                id: index,
                time: result["data"][index].publish_time,
                author:result["data"][index].author
              });
            }
          } else {
            console.log("nodata");
            let obj = document.getElementById("card");
            obj.style.height = "100vh";
          }
        })
        .catch(err => {});
    }
  },
  beforeMount() {
  },
  mounted() {
    this.query(this.$route.path);
  },
  watch: {
    $route(to, from) {
      this.query(this.$route.path);
    }
  }
};
</script>

<style lang = 'less'>
.header {
  font-size: 1.1em;
}
.comment{
  font-size: 1em;
  color: rgb(168, 179, 179);
}
.thisapp {
  .el-input__inner {
    width: 30vw;
    transition: width 1s;
  }
  .el-input__inner:hover {
    width: 50vw;
  }
}
.br {
  height: 10px;
}
.el-card__header {
    padding: 15px 12px;
    border-bottom: 1px solid #EBEEF5;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
}
</style>
