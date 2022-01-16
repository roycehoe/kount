<script lang="ts" setup>import { CreateTimerResponse } from '@/services/survey/getCreateTimerResponse';
import { getDashboardDisplayResponse } from '@/services/survey/getDashboardDisplayResponse';
import { DeleteTimerRequest, getDeleteTimerResponse } from '@/services/survey/getDeleteTimerResponse';
import { onBeforeMount, ref } from 'vue';


const dashboardInfo = ref({} as Array<CreateTimerResponse>)

async function showDashboardInfo() {
  const { ok: isSuccessful, val: response } = await getDashboardDisplayResponse()
  if (isSuccessful) {
    dashboardInfo.value = response as Array<CreateTimerResponse>
    return
  }
  console.error(response)
}

async function deleteTimer(timerId: number) {
  const { ok: isSuccessful, val: response } = await getDeleteTimerResponse({ timer_id: timerId })
  if (isSuccessful) {
    location.reload()
    return
  }
  console.error(response)
}


function showHours(seconds: number) {
  return Math.floor(seconds / 3600) % 24
}

function showMinutes(seconds: number) {
  return Math.floor(seconds / 60) % 60
}

function showSeconds(seconds: number) {
  return Math.floor(seconds) % 60
}


onBeforeMount(async () => await showDashboardInfo());

</script>


<template>
  <div v-for="info in dashboardInfo">
    <div class="survey bg-neutral-100 rounded-md flex flex-row justify-between m-2 bg-gray-50">
      <div class="flex items-center">
        <p class="m-3 font-bold">{{ info.title }}</p>
        <kbd class="kbd font-mono ml-12">
          <p>{{ showHours(info.time) }}h:</p>
          <p>{{ showMinutes(info.time) }}m:</p>
          <p>{{ showSeconds(info.time) }}s</p>
        </kbd>
      </div>

      <div class="flex items-center">
        <button
          class="btn btn-success bg-green-500 m-1 w-16 h-8 rounded-md hover:bg-green-600 border-none min-h-0"
        >View</button>
        <button
          class="btn btn-success bg-red-500 m-1 w-16 h-8 rounded-md hover:bg-red-600 border-none min-h-0"
          @click="deleteTimer(info.id)"
        >Delete</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>