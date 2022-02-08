<template>
  <bar-menu></bar-menu>
  <div v-if="!view && is_local" class="first_visit">
    <div class="info_for_visit"><formUpload></formUpload></div>
    <canvas id="close_info"></canvas>
  </div>
  <div v-else-if="view" class="first_visit_mob">
    <div class="info_for_visit"><formUpload></formUpload></div>
    <canvas id="close_info"></canvas>
  </div>
  <router-view></router-view>
</template>

<script lang="ts">
import barMenu from "@/components/BarMenu.vue";
import formUpload from "@/components/FormUpload.vue";
import { defineComponent, onMounted } from "vue";
import { css } from "@simonwep/selection-js/src/utils";
export default defineComponent({
  name: "App",
  setup() {
    let view = window.matchMedia("(max-width: 600px)").matches;
    const is_local = localStorage.getItem("_Visited") === "true";
    onMounted(() => {
      //TODO: Insert is_local
      if (!view && is_local) {
        const elem_div = document.querySelector<HTMLElement>(".first_visit");
        const info_div = document.querySelector<HTMLElement>(".info_for_visit");
        const close_info = document.querySelector<HTMLCanvasElement>(
          "#close_info"
        );
        if (elem_div !== null && info_div !== null && close_info) {
          const can = close_info.getContext("2d");
          css(elem_div, {
            position: "absolute",
            display: "flex",
            width: "140%",
            height: "100%",
            backgroundColor: "#0000008f",
            zIndex: "11",
          });
          css(info_div, {
            position: "absolute",
            display: "flex",
            width: "40%",
            height: "50%",
            borderRadius: "7% 1%",
            top: "30%",
            overflow: "hidden",
            left: "30%",
            transform: "translate(-50%, -50%)",
            backgroundColor: "GhostWhite",
            zIndex: "12",
          });
          css(close_info, {
            position: "absolute",
            display: "flex",
            width: "25px",
            height: "25px",
            borderRadius: "7px",
            top: "3.5%",
            overflow: "hidden",
            left: "51%",
            transform: "translate(-50%, -50%)",
            backgroundColor: "#1674a787",
            zIndex: "13",
          });
          if (can !== null) {
            const grad = can?.createLinearGradient(-10, -10, 200, 200);
            grad?.addColorStop(0.5, "#f00050");
            grad?.addColorStop(0.1, "#a80038");
            grad?.addColorStop(0.9, "#dd0303");
            grad?.addColorStop(1, "#dd0362");
            can.strokeStyle = grad;
            can.lineWidth = 40;
            can.lineCap = "round";
            can.beginPath();
            can.moveTo(10, 10);
            can.lineTo(290, 140);
            can.stroke();

            can.beginPath();
            can.moveTo(290, 10);
            can.lineTo(10, 140);
            can.stroke();

            close_info.addEventListener("mouseenter", (e) => {
              e.stopPropagation();
              css(close_info, {
                backgroundColor: "#00358a",
              });
            });
            close_info.addEventListener("mouseleave", (e) => {
              e.stopPropagation();
              css(close_info, {
                backgroundColor: "#1674a787",
              });
            });
            close_info.addEventListener("mousedown", (e) => {
              e.stopPropagation();
              css(close_info, {
                transform: "rotate(90deg)",
                backgroundColor: "#4f02a2db",
              });
              css(elem_div, { display: "none" });
              localStorage.setItem("_Visited", "true");
            });
          } else console.error("getContext call failed.");
        } else console.error("Could not find class first_visit.");
      } else if (view) {
        const elem_div = document.querySelector<HTMLElement>(
          ".first_visit_mob"
        );
        const info_div = document.querySelector<HTMLElement>(".info_for_visit");
        const close_info = document.querySelector<HTMLCanvasElement>(
          "#close_info"
        );
        if (elem_div !== null && info_div !== null && close_info) {
          const can = close_info.getContext("2d");
          css(elem_div, {
            position: "absolute",
            display: "flex",
            width: "115%",
            height: "100%",
            backgroundColor: "#0000008f",
            overflow: "hidden",
            zIndex: "11",
          });
          css(info_div, {
            position: "absolute",
            display: "flex",
            width: "60%",
            height: "20%",
            borderRadius: "7% 1%",
            top: "20%",
            overflow: "hidden",
            left: "50%",
            transform: "translate(-50%, -50%)",
            backgroundColor: "GhostWhite",
            zIndex: "12",
          });
          css(close_info, {
            position: "absolute",
            display: "flex",
            width: "20px",
            height: "20px",
            borderRadius: "7px",
            top: "9.3%",
            overflow: "hidden",
            left: "82%",
            transform: "translate(-50%, -50%)",
            backgroundColor: "#1674a787",
            zIndex: "13",
          });
          if (can !== null) {
            const grad = can?.createLinearGradient(-10, -10, 200, 200);
            grad?.addColorStop(0.5, "#f00050");
            grad?.addColorStop(0.1, "#a80038");
            grad?.addColorStop(0.9, "#dd0303");
            grad?.addColorStop(1, "#dd0362");
            can.strokeStyle = grad;
            can.lineWidth = 40;
            can.lineCap = "round";
            can.beginPath();
            can.moveTo(10, 10);
            can.lineTo(290, 140);
            can.stroke();

            can.beginPath();
            can.moveTo(290, 10);
            can.lineTo(10, 140);
            can.stroke();

            close_info.addEventListener("mouseenter", (e) => {
              e.stopPropagation();
              css(close_info, {
                backgroundColor: "#00358a",
              });
            });
            close_info.addEventListener("mouseleave", (e) => {
              e.stopPropagation();
              css(close_info, {
                backgroundColor: "#1674a787",
              });
            });
            close_info.addEventListener("mousedown", (e) => {
              e.stopPropagation();
              css(close_info, {
                transform: "rotate(90deg)",
                backgroundColor: "#4f02a2db",
              });
              css(elem_div, { display: "none" });
              localStorage.setItem("_Visited", "true");
            });
          } else console.error("getContext call failed.");
        } else console.error("Could not find class first_visit.");
      }
    });
    return { view, is_local };
  },
  components: {
    barMenu,
    formUpload,
  },
});
</script>

<style lang="scss">
body {
  background-color: #fff;
  margin: 0;
  padding: 0;
}
#app {
  position: relative;
}
</style>
