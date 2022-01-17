<script lang="ts" setup>
import { getMetricTime, TimerDisplay } from '@/services/timer/convertTime';
import { onBeforeMount, PropType, ref, toRef, watch } from 'vue';

const props = defineProps({
  data: {
    type: Object as PropType<TimerDisplay>
  }
})

const isPaused = ref(false)
const isTimerStarted = ref(false)
const timerDisplay = ref({} as TimerDisplay)


function getTimerDisplay() {
  timerDisplay.value = Object.assign({}, props.data)
}

watch(props, () => getTimerDisplay())

function updateTimerDisplay() {
  const { hours: hours, minutes: minutes, seconds: seconds } = getMetricTime(timerDisplay.value.time)

  timerDisplay.value.hours = hours
  timerDisplay.value.minutes = minutes
  timerDisplay.value.seconds = seconds
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


onBeforeMount(async () => updateTimerDisplay());

</script>


<template>
  <div class="timer-display__centered flex justify-center m-4" v-if="data.title">
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
        >
          <p v-if="!isTimerStarted">Start</p>
          <p v-else>Continue</p>
        </button>
        <button
          class="btn btn-success bg-blue-500 m-1 w-32 h-16 rounded-md hover:bg-blue-600 border-none min-h-0"
          v-else
          @click="isPaused = true"
        >Pause</button>
        <button
          class="btn btn-success bg-red-500 m-1 w-32 h-16 rounded-md hover:bg-red-600 border-none min-h-0"
          @click="() => { getTimerDisplay(); isTimerStarted = false }"
        >Reset</button>
      </div>
    </div>
  </div>
</template>