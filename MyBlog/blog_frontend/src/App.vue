<template>
  
  <div id="app" >
    <div id = "head" class ="head">
      <t></t>
    </div>
    <div id="Menu" class="Menu">
      <m></m>
    </div>
    <div class="main" >
      <div class="b"></div>
      <div class="left"></div>
      <div class="b"></div>
      <div id= "context" class="context" >
        <router-view/>
      </div>
      <div id ="right" class="right"></div>
    </div>
  </div>
</template>

<script>
import m from "@/components/homepage/Menu";
import t from "@/components/homepage/Title";
export default {
  name: 'App',
  components:{m,t},
}
</script>

<style lang="less">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;

  
  /* margin-top: 60px; */
}

body{
	margin: 0; 
	padding: 0;
	border: 0;
}
div{
  // border-style:solid;
  // border-width:1px;
}
.head{
  height: 80px;
}
.main{
   display: flex;
  //  background-size: 100% 100%;
  background-color: rgba(101, 145, 182, 0.2);
  // width: 100vw;
  
}
.right{
   width: 30%;

}
.left{
  width: 30%;
}
.Menu{
    width: 100%;

    background-color: cadetblue;
}
.context{
  width: 80vW;
}
.b{
  width:30px;
}
</style>
