<script lang="ts" setup>import { getMetricTime, showHours, showMinutes, showSeconds } from '@/services/timer/convertTime';
import { CreateTimerResponse } from '@/services/timer/getCreateTimerResponse';
import { getDashboardDisplayResponse } from '@/services/timer/getDashboardDisplayResponse';
import { getDeleteTimerResponse } from '@/services/timer/getDeleteTimerResponse';
import { onBeforeMount, ref } from 'vue';


interface DashboardInfoDisplay {
  id: number
  title: string
  createdAt: any
  hours: number
  minutes: number
  seconds: number
}


const dashboardInfo = ref([] as Array<DashboardInfoDisplay>)


function createDashboardDisplay(createTimerResponse: Array<CreateTimerResponse>) {
  createTimerResponse.forEach(element => {
    console.log(element.id)
    dashboardInfo.value.push({
      id: element.id,
      title: element.title,
      createdAt: element.created_at,
      hours: getMetricTime(element.time).hours,
      minutes: getMetricTime(element.time).minutes,
      seconds: getMetricTime(element.time).seconds,
    })
  })
}



async function showDashboardInfo() {
  const { ok: isSuccessful, val: response } = await getDashboardDisplayResponse()
  if (isSuccessful) {
    const createTimerResponse = response as Array<CreateTimerResponse>
    createDashboardDisplay(createTimerResponse)
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



onBeforeMount(async () => await showDashboardInfo());

</script>


<template>
  {{ dashboardInfo }}
  <div v-for="info in dashboardInfo">
    <div class="survey bg-neutral-100 rounded-md flex flex-row justify-between m-2 bg-gray-50">
      <div class="flex items-center">
        <p class="m-3 font-bold">{{ info.title }}</p>
      </div>

      <div class="flex items-center">
        <kbd class="kbd font-mono mr-36">
          <p>{{ info.hours }}h:</p>
          <p>{{ info.minutes }}m:</p>
          <p>{{ info.seconds }}s</p>
        </kbd>
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