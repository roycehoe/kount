<script lang="ts" setup>
import { TimerDisplay } from '@/services/timer/convertTime';
import { PropType, ref } from 'vue';


const props = defineProps({
  data: {
    type: Object as PropType<TimerDisplay>
  }
})


interface getCreateTimerResponse {
  title: string
  totalSeconds: number //need two variables like time left and total time
}

interface GetTimerDisplay {
  title: string,
  hours: number,
  minutes: number,
  seconds: number
}

const timerDisplay = ref({
  id: 1,
  title: "placeholder",
  createdAt: 1,
  hours: 0,
  minutes: 0,
  seconds: 30,
  time: 30
} as TimerDisplay)



const isPaused = ref(false)
const isTimerStarted = ref(false)



function updateTimerDisplay() {
  timerDisplay.value.title = timerDisplay.value.title;
  timerDisplay.value.hours = Math.floor(timerDisplay.value.time / 3600) % 24;
  timerDisplay.value.minutes = Math.floor(timerDisplay.value.time / 60) % 60;
  timerDisplay.value.seconds = Math.floor(timerDisplay.value.time) % 60;
}

function startCountdown() {
  isPaused.value = false
  isTimerStarted.value = true

  const timer = setInterval(() => {
    if (timerDisplay.value.time < 0) {
      clearInterval(timer)
      timerDisplay.value.time = 0
      updateTimerDisplay()
      return
    }
    if (isPaused.value) {
      clearInterval(timer)
      updateTimerDisplay()
      return
    }

    timerDisplay.value.time -= 1
    updateTimerDisplay()
  }, 1000)
}


updateTimerDisplay()

</script>


<template>
  <p>timer data: {{ data }}</p>
  <div class="timer-display__centered flex justify-center m-4">
    <div class="timer-display flex flex-col">
      <div class="timer__header">
        <p class="text-center font-bold text-2xl">{{ timerDisplay.title }}</p>
      </div>
      <div class="divider"></div>
      <div class="grid grid-flow-col gap-5 text-center auto-cols-max">
        <div class="flex flex-col">
          <span class="font-mono text-8xl countdown">
            <span :style="{ '--value': timerDisplay.hours }"></span>
          </span>
          hours
        </div>
        <div class="flex flex-col">
          <span class="font-mono text-8xl countdown">
            <span :style="{ '--value': timerDisplay.minutes }"></span>
          </span>
          min
        </div>
        <div class="flex flex-col">
          <span class="font-mono text-8xl countdown">
            <span :style="{ '--value': timerDisplay.seconds }"></span>
          </span>
          sec
        </div>
      </div>
      <div class="timer-buttons flex flex-row justify-evenly mt-8">
        <button
          class="btn btn-success bg-green-500 m-1 w-32 h-16 rounded-md hover:bg-green-600 border-none min-h-0"
          v-if="isPaused || !isTimerStarted"
          @click="startCountdown"
        >Start</button>
        <button
          class="btn btn-success bg-blue-500 m-1 w-32 h-16 rounded-md hover:bg-blue-600 border-none min-h-0"
          v-else
          @click="isPaused = true"
        >Pause</button>
        <button
          class="btn btn-success bg-red-500 m-1 w-32 h-16 rounded-md hover:bg-red-600 border-none min-h-0"
        >Reset - This button actually sends a get request</button>
      </div>
    </div>
  </div>
</template>