<template>
  <Navigation/>
  <router-view/>
  <Toast />
</template>


<script>
import axios from 'axios'
import Navigation from './components/Navigation.vue'
import Toast from '@/components/Toast.vue'
import { useUserStore } from '@/stores/user'
export default{
  setup() {
    const userStore = useUserStore()
    return {
      userStore
    }
  },
  components: {
    Toast,
    Navigation,
  },
  beforeCreate() {
    this.userStore.initStore()
    const token = this.userStore.user.access
    if (token) {
        axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    }else {
      axios.defaults.headers.common["Authorization"] = " ";
    }
  }
}
</script>
<style>
body{
  background-color: rgb(33, 33, 33);
}

</style>
