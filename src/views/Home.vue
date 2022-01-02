<script lang="ts" setup>
import { getAssetUrl } from '@/services/assets';

</script>

<template>
  <div class="display">
    <div class="display--flexboxColumn display--onGrid">
      <div class="logo">
        <img class="logo--smallImg" :src="getAssetUrl('graphics', 'logo.png')" />
      </div>

      <div class="display--inputBox">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>