<script lang="ts" setup>
import { getAssetUrl } from '@/services/assets';


</script>

<template>
  <div class="display w-2/12 mt-16 p-2 m-auto">
    <img :src="getAssetUrl('graphics', 'logo.png')" />
    <div class="display--inputBox mt-8">
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>