<script lang="ts" setup>
import { getAssetUrl } from '@/services/assets';


</script>

<template>
  <div class="display">
    <div class="display--flexboxColumn display--onGrid">
      <div class="display--inputBox mt-40">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.logo {
  display: flex;
  justify-content: center;
  margin-bottom: 5vh;
  &--smallImg {
    width: 200px;
  }
}

.display {
  margin: auto;
  width: 20%;
  margin-top: 10vh;
  padding: 10px;
}
</style>