<script lang="ts" setup>
import { ref } from 'vue';

interface getCreateTimerResponse {
  title: string
  totalSeconds: number
}

interface GetTimerDisplay {
  title: string,
  hours: number,
  minutes: number,
  seconds: number
}



const timerResponse = ref({
  title: "placeholder",
  totalSeconds: 3
} as getCreateTimerResponse)

const timerDisplay = ref({
} as GetTimerDisplay)


const isPaused = ref(false)

function setTimer() {
  timerDisplay.value.hours = Math.floor(timerResponse.value.totalSeconds / 3600) % 24;
  timerDisplay.value.minutes = Math.floor(timerResponse.value.totalSeconds / 60) % 60;
  timerDisplay.value.seconds = Math.floor(timerResponse.value.totalSeconds) % 60;
}

function startCountdown() {
  const countdown = setInterval(() => {
    timerResponse.value.totalSeconds -= 1
    setTimer()
  }, 1000)
  if (timerResponse.value.totalSeconds == 0) {
    clearInterval(countdown)
    timerResponse.value.totalSeconds = 0
    setTimer()
  }
}

function stopCountdown() {
}

function resetCountdown() {
}

setTimer()

</script>


<template>
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
          v-if="isPaused"
          @click="isPaused = false"
        >Start</button>
        <button
          class="btn btn-success bg-blue-500 m-1 w-32 h-16 rounded-md hover:bg-blue-600 border-none min-h-0"
          v-else
          @click="isPaused = true"
        >Pause</button>
        <button
          class="btn btn-success bg-red-500 m-1 w-32 h-16 rounded-md hover:bg-red-600 border-none min-h-0"
        >Reset</button>
        <button
          class="btn btn-success bg-red-500 m-1 w-32 h-16 rounded-md hover:bg-red-600 border-none min-h-0"
          @click="startCountdown"
        >TEST BUTTON</button>
      </div>
    </div>
  </div>
</template>