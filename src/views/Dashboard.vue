<script lang="ts" setup>
import SurveyList from '@/components/SurveyList.vue';
import { ref } from 'vue';
import SurveyCreateMenu from '@/components/SurveyCreateMenu.vue';

</script>

<template>
  <div class="min-h-full">
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
      </div>
    </div>
    <div>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <SurveyCreateMenu></SurveyCreateMenu>
        <div class="min-h-full">
          <div>
            <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
              <!-- Replace with your content -->
              <div class="px-4 py-6 sm:px-0">
                <div class="border-4 border-dashed border-gray-200 rounded-lg h-96">
                  <SurveyList></SurveyList>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>