<script lang="ts" setup>import { getDashboardDisplayResponse, GetDashboardDisplayResponse } from '@/services/survey/getDashboardDisplayResponse';
import { getDeleteSurveyResponse } from '@/services/survey/getDeleteSurveyResponse';
import { onBeforeMount, ref } from 'vue';


const surveyLink = ref("another")
const dashboardInfo = ref({} as GetDashboardDisplayResponse)


onBeforeMount(async () => await showDashboardInfo());

</script>


<template>
  <div>
    <div class="survey bg-neutral-100 rounded-md flex flex-row justify-between m-2 bg-gray-50">
      <div class="flex items-center">
        <p class="m-3">Timer title</p>
        <kbd class="kbd font-mono ml-12">1h:12m:10s</kbd>
      </div>

      <div class="flex items-center">
        <button
          class="btn btn-success bg-green-500 m-1 w-16 h-8 rounded-md hover:bg-green-600 border-none min-h-0"
        >View</button>
        <button
          class="btn btn-success bg-red-500 m-1 w-16 h-8 rounded-md hover:bg-red-600 border-none min-h-0"
        >Delete</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>