<template>
  <form v-if="isInitial" enctype="multipart/form" novalidate>
    <div v-if="isInitial" :limits="(cur_sq = total)" class="box_for_up">
      <input
        type="file"
        multiple
        :name="uploadFieldName"
        @change.stop="filesChange($event, $event.target.files)"
        accept="image/*"
        class="input_file"
      />
      <p v-if="total_cubes.total.size === 0">Drag files or click to browse</p>
      <!-- <p v-if="isSvaing">
        Compression <br />
        {{ total_cubes.progress }}%
      </p> -->
      <p v-else-if="cur_sq <= avaible">Total: {{ total }} squares</p>
      <p v-else class="error_limit" :add_plur="plur">
        Sorry, avaible squares are: {{ avaible }} <br />
        your picture{{ plur }}needs: {{ cur_sq }}. Resize or I'll crop.
      </p>
    </div>
  </form>
  <div v-if="isInitial" class="div_cont_name_file"></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  check_file,
  send_file,
  Cubes,
  ass_elem,
  ass_elemNS,
  add_events,
} from "./functions";

const STATUS_INITIAL = 0,
  STATUS_SAVING = 1,
  STATUS_SUCCESS = 2,
  STATUS_FAILED = 3;

export default defineComponent({
  name: "app",
  setup() {
    let avaible = 600;
    const position = { top: 0, left: 184 };
    //TODO Make an api for total avaible elements and
    return { avaible, position };
  },
  data() {
    return {
      uploadError: null,
      uploadFieldName: "file",
      top_pos: -6,
      total_cubes: {
        total: new Map(),
        to_commit: "False",
        progress: 0,
        currentStatus: 0,
      },
    };
  },
  computed: {
    isInitial(): boolean {
      return this.total_cubes.currentStatus === STATUS_INITIAL;
    },
    isSaving(): boolean {
      return this.total_cubes.currentStatus === STATUS_SAVING;
    },
    isSuccess(): boolean {
      return this.total_cubes.currentStatus === STATUS_SUCCESS;
    },
    isFailed(): boolean {
      return this.total_cubes.currentStatus === STATUS_FAILED;
    },
    total(): number {
      let toRet = 0;
      this.total_cubes.total.forEach((val) => {
        toRet += (val as Cubes).cubes;
      });
      return toRet;
    },
    plur() {
      if (this.total_cubes.total.size > 1) {
        return "s ";
      }
      return " ";
    },
  },
  methods: {
    reset() {
      // reset form to initial state
      this.total_cubes.currentStatus = STATUS_INITIAL;
      this.uploadError = null;
      this.total_cubes.total.clear();
    },
    filesChange(event: Event, fileList: FileList) {
      // handle file changes
      const chars = [..."ABCDEFGHIJKLMNOPQRSTUVWXYZ"];
      // and then just do:
      const class_name = [...Array(5)]
        .map((i) => chars[(Math.random() * chars.length) | 0])
        .join(``);
      if (!fileList.length) {
        this.total_cubes.currentStatus = STATUS_FAILED;
        console.error("File Not Found.");
        return;
      }
      //DO NOT ADD EXTRA ELEMENT YOU WILL BROKE PARENT SIBILING RELETIONSHIP
      check_file(fileList, this.total_cubes);
      for (let i = 0; i < fileList.length; i++) {
        if (this.total_cubes.total.has(fileList[i].name)) {
          continue;
        }
        ass_elem(
          ".div_cont_name_file",
          "p",
          fileList[i].name,
          "font-size: 0.7rem;text-overflow: ellipsis;margin: -6px;padding: 0;width: 90%; text-align: left;display: -webkit-box;-webkit-box-orient: vertical;-webkit-line-clamp: 1; /* number of lines to show */line-height: 1.1; /* fallback */max-height: 1;overflow: hidden;user-select: none;",
          undefined
        );
        ass_elemNS(
          ".div_cont_name_file",
          "svg",
          "http://www.w3.org/2000/svg",
          `position: relative;display: block;height: 12px;width:10px;top:${this.top_pos}px;left:100%;z-index: 3;`,
          {
            class: `${class_name + i}`,
            version: "1.1",
            viewBox: "0 0 512 512",
            ["xml:space"]: "preserve",
            xmlns: "http://www.w3.org/2000/svg",
          }
        );
        ass_elemNS(`.${class_name + i}`, "g", "http://www.w3.org/2000/svg");
        ass_elemNS(
          `.${class_name + i} g`,
          "path",
          "http://www.w3.org/2000/svg",
          undefined,
          {
            d:
              "m443.6 387.1-131.2-131.7 131.5-130c5.4-5.4 5.4-14.2 0-19.6l-37.4-37.6c-2.6-2.6-6.1-4-9.8-4s-7.2 1.5-9.8 4l-130.9 129.6-131.1-129.5c-2.6-2.6-6.1-4-9.8-4s-7.2 1.5-9.8 4l-37.3 37.6c-5.4 5.4-5.4 14.2 0 19.6l131.5 130-131.1 131.6c-2.6 2.6-4.1 6.1-4.1 9.8s1.4 7.2 4.1 9.8l37.4 37.6c2.7 2.7 6.2 4.1 9.8 4.1 3.5 0 7.1-1.3 9.8-4.1l130.6-131.2 130.7 131.1c2.7 2.7 6.2 4.1 9.8 4.1 3.5 0 7.1-1.3 9.8-4.1l37.4-37.6c2.6-2.6 4.1-6.1 4.1-9.8-0.1-3.6-1.6-7.1-4.2-9.7z",
          }
        );
        const elem = document.querySelector(`.${class_name + i} g`);

        add_events(elem as Element, ["mousedown", "touchstart"], (e) => {
          e.stopPropagation();
          e.preventDefault();
          if (
            !this.total_cubes.total.delete(
              ((((e.target as HTMLElement).parentNode as HTMLElement)
                .parentNode as HTMLElement).previousSibling as HTMLElement)
                .innerHTML
            )
          ) {
            console.error("Did not delete from Map.");
          }
          ((((e.target as HTMLElement).parentNode as HTMLElement)
            .parentNode as HTMLElement)
            .previousSibling as HTMLElement).remove();

          (((e.target as HTMLElement).parentNode as HTMLElement)
            .parentNode as HTMLElement).remove();
        });
        add_events(elem as Element, ["mouseover", "mouseenter"], (e) => {
          e.preventDefault();
          e.stopPropagation();
          if (
            ((e.target as HTMLElement).firstElementChild as HTMLElement) ===
            null
          ) {
            return;
          }
          ((e.target as HTMLElement)
            .firstElementChild as HTMLElement).style.setProperty(
            "fill",
            "#f0005c"
          );
        });
        add_events(elem as Element, ["mouseleave"], (e) => {
          e.preventDefault();
          e.stopPropagation();
          if (
            ((e.target as HTMLElement).firstElementChild as HTMLElement) ===
            null
          ) {
            return;
          }
          ((e.target as HTMLElement)
            .firstElementChild as HTMLElement).style.setProperty(
            "fill",
            "#000000"
          );
        });
      }
      //this.total_cubes.currentStatus = STATUS_SAVING;
      //send_file(fileList, this.total_cubes);
    },
  },
  mounted() {
    const inp_ele = document.querySelector(".input_file");
    add_events(inp_ele as Element, ["click", "touchstart"], (e) => {
      e.stopPropagation();
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (e as any).target.value = null;
    });
    this.reset();
  },
});
</script>

<style scoped lang="scss">
.box_for_up {
  outline: 2px dashed grey; /* the dash box */
  display: flex;
  flex-direction: column;
  flex-grow: column;
  user-select: none;
  position: relative;
  margin: 0;
  top: 2%;
  left: 0;
  outline-offset: -6px;
  color: rgb(80, 80, 80);
  padding: 5% 5%;
  min-height: 50%; /* minimum height */
  position: relative;
  outline-style: bold;
  cursor: pointer;
}
form {
  position: relative;
  top: 85%;
  width: 35%;
  left: 30%;
  height: 12%;
}
.input_file {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 74px;
  position: absolute;
  top: 0%;
  left: 0%;
  cursor: pointer;
}

.box_for_up:hover {
  background: #312c2c23;
  border-radius: 6%;
}
.div_cont_name_file {
  position: absolute;
  left: 66%;
  top: 86.5%;
  width: 24%;
  text-overflow: ellipsis;
  cursor: default;
}

div p {
  font-size: 1em;
  text-align: center;
  flex-flow: column wrap;
  padding: 1% 0;
  margin: 0;
  margin: 0;
  cursor: pointer;
}
.error_limit {
  color: rgba(202, 0, 0, 0.993);
  min-height: 1%;
}
@media screen and (max-width: 600px) {
  div ~ div p,
  .error_limit {
    font-size: 0.56rem;
  }
  form {
    position: relative;
    top: 70%;
    width: 65%;
    left: 17%;
    height: 12%;
  }
  .input_file {
    height: 100%;
  }
  .div_cont_name_file {
    left: 66%;
    top: 5.5%;
  }
}
</style>
