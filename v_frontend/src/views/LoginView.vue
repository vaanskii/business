<template>
    <section class="bg-gray-100 mt-8">
  <div class="flex flex-col items-center px-6 py-8 mx-auto md:h-screen lg:py-10 fixed w-full ">
      <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          Business    
      </a>
      <div class="w-full rounded-lg shadow-2xl dark:border md:mt-0 sm:max-w-md xl:p-0 dark:border-gray-100 drop-shadow-2xl">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-gray-100">
                    Login
              </h1>
              <hr class="">
              <form class="space-y-4 md:space-y-6" v-on:submit.prevent="submitForm">
                  <div>
                    <input type="text" name="username" v-model="form.username" id="username" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100" placeholder="Enter your username">
                  </div>
                  <div>
                    <input type="password" name="password" v-model="form.password" id="password" placeholder="••••••••" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100">
                  </div>
                  <div class="flex items-start">
                      <div class="flex items-center h-5">
                        <input id="terms" aria-describedby="terms" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-100focus:ring-3 focus:ring-primary-300 dark:bg-gray-100 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800">
                      </div>
                      <div class="ml-3 text-sm">
                        <label for="terms" class="font-light text-gray-900 dark:text-gray-100">Remember me</label>
                      </div>
                  </div>
                  <button type="submit" class="w-full shadow-lg text-gray-100 border bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 hover:bg-black hover:text-white transition ease-in-out hover:-translate-y-1 hover:scale-100">Login</button>
                  <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                      Do not have an account? <a href="/signup" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Login here</a>
                  </p>

                  <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                  </template>

              </form>
          </div>
      </div>
  </div>
</section>
</template>

<script>
import router from '@/router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
export default {
  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
  },
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      errors: []
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.form.username === ''){
        this.errors.push('your email is missing')
      }

      if (this.form.password === '') {
        this.errors.push('your password is missing')
      }

      if(this.errors.length === 0){
        await axios
                  .post('/api/login/', this.form)
                  .then(response => {
                      this.userStore.setToken(response.data)

                      axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                  })
                  .catch(error => {
                    console.log('error', error.message)
                    this.errors.push('The username or password is incorrect')
                  })
      if (this.errors.length === 0) {
        await axios
                  .get('/api/me')
                  .then(response => {
                    this.userStore.setUserInfo(response.data)
                    this.$router.push('/')
                  })
                  .catch(error => {
                    console.log('error', error.message)
                  })
      }
      }
    }
  }
}
</script>