<template>
  <div class="background-color">
      <div class="flex flex-col items-center ml-96 h-full justify-center">
        <h1 class="responsive text-white text-7xl mt-[500px] absolute ">ClearView Creations</h1>
        <p class="responsive-p text-white text-3xl w-[600px] mt-[900px] absolute">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eaque blanditiis dolor fugiat. Voluptatum modi, cumque nostrum molestias quaerat corporis reprehenderit esse, saepe repellendus ullam temporibus velit tempora perferendis? Praesentium, amet!</p>
        </div>
      <div class="background">
      </div>
    </div>
    <div>
      <Carousel/>
      <div class="flex justify-center items-center mb-40">
        <div class="w-[800px]">
          <p class="p-responsive text-gray-500 dark:text-gray-100 text-lg">Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.</p>
          <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
          <p class="p-responsive text-gray-500 dark:text-gray-100 text-lg">Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.</p>
        </div>
      </div>
      <ImageGallery/>
      <Footer />
  </div>
</template>
  
<script>
import Carousel from '@/components/Carousel.vue';
import ImageGallery from '@/components/ImageGallery.vue';
import Footer from '@/components/Footer.vue'
export default {
  components: {
    Carousel,
    ImageGallery,
    Footer
  }
}
</script>
  
  <style>
  .background {
    height: 95vh;
    width: 50vw;
    background-image: url(../assets/background.jpg);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    overflow: hidden;
  }
  
  .background-color {
    background-color: #4a4b4d;
  }
  @media (max-width:1024px){
    .responsive{
      font-size: 2.5rem; 
      line-height: 2rem;
    }
    .responsive-p{
      font-size: 1.5rem; 
      line-height: 2.5rem;
      width: 500px;
      margin-left: 80px;
    }
    .p-responsive{
      font-size: 1.5rem;
      text-align:center;
      line-height: 2.5rem;
    }
  }
  @media (max-width:911px){
    
    .responsive{
        font-size: 1.2rem; 
        line-height: 1.7rem;
        margin-right: 140px;
        width: 250px;
        margin-left:40px;
    }
    .responsive-p{
        font-size: 0.9rem; 
        line-height: 1.7rem;
        margin-right: 200px;
        width: 200px;
        margin-left:40px;
    } 
  }
  @media (max-width:440px){
    .background{
      background-image:none;
      height: 400px;
      margin-bottom: 50px;
    } 
    .responsive{
        font-size: 1.5rem; 
        line-height: 1.7rem;
        margin-right: 400px;
        width: 240px;
        margin-top:80px;
    }
    .responsive-p{
        font-size: 0.7rem; 
        line-height: 1.7rem;
        margin-right: 420px;
        width: 200px;
        margin-top: 400px;
    }
    
  }
  
  @media (max-width:330px) {
    .background{
      background-image:none;
      height: 400px;
      margin-bottom: 50px;
      
    }
    .responsive{
        font-size: 1.2rem; 
        line-height: 1.7rem;
        margin-right: 500px;
        width: 180px;
        margin-top:80px;
    }
    .responsive-p{
        font-size: 0.7rem; 
        line-height: 1.7rem;
        margin-right: 470px;
        width: 200px;
        margin-top: 400px;
    }
  }
  </style>
  