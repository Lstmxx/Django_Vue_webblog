<template>
<div class="details_bc">
  <div class="details_title">
    <div class="paper_title">{{title}}</div>
    <div class="paper_author">{{author}}</div>
    <div class="paper_time">{{time}}</div>
   <hr style="height:1px;border:none;border-top:1px solid lightgray;" />
  </div>

  <div v-html="html" class="details_body"></div>
</div>
</template>

<script>

import hljs from 'highlight.js'
import 'highlight.js/styles/atom-one-dark.css'
const highlightCode = () => {
  const preEl = document.querySelectorAll('pre')
  preEl.forEach((el) => {
    hljs.highlightBlock(el)
  })
}

export default {
  name: "Details",
  data() {
    return {
      html:'',
      title:'',
      author:'',
      time:'',
    };
  },
  mounted() {
     //console.log(this.$route.query.id);
     this.$axios.post('/get_paper_by_id',{
       id:this.$route.query.id
     }).then((result) => {
      console.log(result['data']);
      this.html = result['data'][0].data
      this.title = result['data'][0].name
      this.author = "作者:"+result['data'][0].author_id
      this.time = "发布时间:"+result['data'][0].publish_time
    }).catch((err) => {
       
    });
    // this.$axios.post('/test',{}).then((result) => {
    //   console.log(result['data'][0].html);
    //   this.html = result['data'][0].html
    // }).catch((err) => {
       
    // });
    highlightCode();
  },
  updated() {
    highlightCode();
  },
};
</script>
<style lang = 'less'>
.line{
 color: cornsilk;
 size: 100
}
.details_title{
  width: 90%;
  margin: auto;
  
}
.details_bc{
  margin-top: 10px;
  background-color: rgb(255, 255, 247);
  width: 100%;
}
.details_body{
  width: 90%;
  margin: auto;
}
  .paper_title{
    font-size: 37px;
    font-weight: 700;

  }
</style>
