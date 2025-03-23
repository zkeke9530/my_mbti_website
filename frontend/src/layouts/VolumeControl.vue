<template>
  <div class="volume-control" @click="toggleVolume">
    <img :src="currentIcon" alt="音量控制" class="volume-icon" />
  </div>
</template>

<script setup>
import { ref, inject, watch, computed } from 'vue'
import volumeOnIcon from '@/assets/volume_on.png'
import volumeOffIcon from '@/assets/volume_off.png'

// 从全局中注入音量状态（默认应在 provide 中设为 1）
const globalVolume = inject('globalVolume')

// 定义局部音量变量，初始值同步全局音量
const localVolume = ref(globalVolume.value)

// 监听局部变量变化，同步更新全局音量
watch(localVolume, (newVolume) => {
  globalVolume.value = newVolume
})

// 同步全局状态变化到局部变量（双向绑定）
watch(globalVolume, (newVolume) => {
  localVolume.value = newVolume
})

// 根据音量状态计算当前显示的图标，音量大于 0 显示开启图标，否则显示关闭图标
const currentIcon = computed(() =>
  localVolume.value > 0 ? volumeOnIcon : volumeOffIcon
)

// 切换音量状态：如果当前音量大于 0，则点击后关闭声音（设置为 0）；否则开启声音（设置为 1）
const toggleVolume = () => {
  localVolume.value = localVolume.value > 0 ? 0 : 1
}
</script>

<style scoped>
.volume-control {
  display: flex;
  justify-content: flex-end;  /* 将内容放在容器的最右侧 */
  align-items: center;
  cursor: url('src/assets/cursor_click.png'), pointer;
}

.volume-icon {
  width: 28px;
  height: 20px;
}
</style>
