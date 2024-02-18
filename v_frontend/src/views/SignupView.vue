<template>
    <section class="bg-gray-100 mt-8">
  <div class="flex flex-col items-center px-6 py-8 mx-auto md:h-screen lg:py-10 fixed w-full">
      <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          Business    
      </a>
      <div class="w-full rounded-lg shadow-2xl dark:border md:mt-0 sm:max-w-md xl:p-0 dark:border-gray-100 drop-shadow-2xl">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-100 md:text-2xl dark:text-gray-100">
                  Create an account
              </h1>
              <hr class="">
              <form class="space-y-4 md:space-y-6" v-on:submit.prevent="submitForm">
                  <div>
                      <input type="email"  v-model="form.email" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100" placeholder="Enter your email">
                  </div>
                  <div>
                      <input type="text" v-model="form.username" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100" placeholder="Enter your username">
                  </div>
                  <div>
                    <select  v-model="form.city" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100">
                        <option value="batumi">Batumi</option>
                        <option value="tbilisi">Tbilisi</option>
                        <option value="kutaisi">Kutaisi</option>
                    </select>
                  </div>
                  <div>
                      <input type="password" v-model="form.password1" placeholder="••••••••" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100">
                  </div>
                  <div>
                      <input type="password" v-model="form.password2" placeholder="Confirm password" class="sm:text-sm rounded-lg  w-full p-2.5 dark:bg-transparent border dark:border-gray-100 dark:placeholder-gray-100 dark:text-gray-100">
                  </div>
                  <div class="flex items-start">
                      <div class="flex items-center h-5">
                        <input id="terms" aria-describedby="terms" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-100 focus:ring-3 focus:ring-primary-300 dark:bg-gray-100 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800">
                      </div>
                      <div class="ml-3 text-sm">
                        <label for="terms" class="font-light dark:text-gray-100">I accept the <a class="font-medium text-primary-600 hover:underline dark:text-primary-500" href="#">Terms and Conditions</a></label>
                      </div>
                  </div>
                  <button type="submit" class="w-full shadow-lg text-gray-100 border bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 hover:bg-black hover:text-white transition ease-in-out hover:-translate-y-1 hover:scale-100">Create an account</button>
                  <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                      Already have an account? <a href="/login" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Login here</a>
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
import axios from 'axios'
import { useToastStore } from '@/stores/toast.js'
import router from '@/router'

export default{
    setup() {
        const toastStore = useToastStore()
        
        return {
            toastStore,
        }
    },
    data() {
        return {
            form: {
                email: '',
                username: '',
                password1: '',
                password2: '',
                city: 'batumi'
            },
            errors : []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('your email is missing')
            }

            if (this.form.username === '') {
                this.errors.push('your username is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }
            if (this.errors.length === 0) {
               axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please login ', 'bg-emerald-100')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                            this.form.city = 'batumi'
                        } else{
                            const data = JSON.parse(response.data.message)
                            for (const key in data) {
                                this.errors.push(data[key][0].message)
                            }
                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                        console.log(response.data)

                    })
                    .catch(error => {
                        console.log('error',error)
                    })
            }
        }
    }
}
</script>