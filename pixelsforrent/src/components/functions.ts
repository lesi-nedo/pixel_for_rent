type ToRight = (
  direc: boolean,
  elem: HTMLElement | null,
  view: boolean,
  what_path: number
) => void;

export const toRightMenu: ToRight = (direc, elem, view, what_path) => {
  //true is letf current false is right
  if (elem === null) {
    console.error("No Element matched.");
    return;
  }
  //ORDER COUNTS
  window.localStorage.setItem("_PosBar", String(direc));
  const stylesheet = document.styleSheets[1];
  const styleFor_home = document.styleSheets[0];
  switch (what_path) {
    case 0:
      style_home(styleFor_home, view, direc);
      break;
  }
  let rule;
  if (view) {
    if (direc) {
      ((stylesheet.cssRules[12] as CSSMediaRule)
        .cssRules[1] as CSSStyleRule).style.setProperty("left", "-4.3%");
    } else {
      ((stylesheet.cssRules[12] as CSSMediaRule)
        .cssRules[1] as CSSStyleRule).style.setProperty("left", "15.1vmin");
    }
  }
  if (direc) {
    elem.style.left = "auto";
    elem = elem.querySelector("svg[id=ToRight-button]");
    if (elem != null) {
      elem.style.transform = "scaleX(-1)";
    } else {
      console.error("No ELement Matched In The Function toRigthMenu.");
      return;
    }
    (stylesheet.cssRules[3] as CSSStyleRule).style.setProperty("left", "-11%");
  } else {
    elem.style.left = "0";
    elem = elem.querySelector("svg[id=ToRight-button]");
    if (elem != null) {
      elem.style.transform = "scaleX(1)";
    } else {
      console.error("No ELement Matched In The Function toRigthMenu.");
      return;
    }
    (stylesheet.cssRules[3] as CSSStyleRule).style.setProperty(
      "left",
      "9.105vmin"
    );
  }
};

const style_home = (
  styleFor_home: CSSStyleSheet,
  view: boolean,
  direc: boolean
) => {
  if (!view) {
    if (!direc) {
      ((styleFor_home.rules[0] as CSSMediaRule)
        .cssRules[0] as CSSStyleRule).style.setProperty("left", "10vmin");
      ((styleFor_home.rules[0] as CSSMediaRule)
        .cssRules[0] as CSSStyleRule).style.setProperty("width", "2500px");
    } else {
      ((styleFor_home.rules[0] as CSSMediaRule)
        .cssRules[0] as CSSStyleRule).style.setProperty("width", "2583px");
      ((styleFor_home.rules[0] as CSSMediaRule)
        .cssRules[0] as CSSStyleRule).style.setProperty("left", "-0.1%");
    }
  } else if (view) {
    if (!direc) {
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[0] as CSSStyleRule).style.setProperty("left", "16%");
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[0] as CSSStyleRule).style.setProperty("left", "16vmin");
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[1] as CSSStyleRule).style.left = "1.3%";
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[1] as CSSStyleRule).style.left = "1.3vmin";
    } else {
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[1] as CSSStyleRule).style.left = "-14.5%";
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[1] as CSSStyleRule).style.left = "-14.5vmin";
    }
  }
  if (!view) {
    if (direc) {
      ((styleFor_home.rules[0] as CSSMediaRule)
        .cssRules[3] as CSSStyleRule).style.setProperty("left", "auto");
    } else {
      ((styleFor_home.rules[0] as CSSMediaRule)
        .cssRules[3] as CSSStyleRule).style.setProperty("left", ".6vmin");
    }
  } else if (view) {
    if (direc) {
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[2] as CSSStyleRule).style.setProperty("left", "98.5%");
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[2] as CSSStyleRule).style.setProperty("left", "99vmin");
    } else {
      ((styleFor_home.rules[1] as CSSMediaRule)
        .cssRules[2] as CSSStyleRule).style.setProperty("left", "-1.9vmin");
    }
  }
};

/* CHECK IS FILE IS OF CORRECT SIZE 
  @Param: file
  @Ret: boolean

*/
const AREA = 11 * 11;

export interface Cubes {
  cubes: number;
  file: Blob;
  fileName: string;
}

interface Total_cubes {
  total: Map<string, Cubes>;
  to_commit: string;
  progress?: number;
  currentStatus: number;
}

type Send_file = (file: FileList, total_squares: Total_cubes) => void;

export const send_file: Send_file = (file: FileList, total_squares) => {
  import("compressorjs")
    .then((Compressor) => {
      for (let i = 0; i < file.length; i++) {
        let type = "0";
        if (file[i].type === "image/gif") type = "image/gif";
        else type = "image/png";
        new Compressor.default(file[i], {
          quality: 0.85,
          maxWidth: 2500,
          maxHeight: 1260,
          mimeType: type,
          convertSize: Infinity,
          success(result) {
            const formData = new FormData();
            /* eslint-disable  @typescript-eslint/no-explicit-any */
            formData.append("file", result, (result as any).name);
            import("./async_call")
              .then((fun) => {
                fun
                  .upload(
                    formData,
                    (event) => {
                      total_squares.progress = Math.round(
                        (100 * event.loaded) / event.total
                      );
                    },
                    total_squares.to_commit
                  )
                  .catch((e) => {
                    console.error("Could Not Upload Files. " + e);
                    total_squares.currentStatus = 3;
                  });
                if (i == file.length && total_squares.currentStatus !== 3)
                  total_squares.currentStatus = 2;
              })
              .catch((e) => {
                console.error("Could Not Upload Files. " + e.message);
                total_squares.currentStatus = 3;
                return;
              });
          },
          error(err) {
            total_squares.currentStatus = 3;
            console.error("Could Not Compress File. Error: " + err);
          },
        });
      }
    })
    .catch((e) =>
      console.error("Compressorjs library could not been fetched. Reason: " + e)
    );
};

type Check_file = (file: FileList, total_cubes: Total_cubes) => number;

export const check_file: Check_file = (files, total_cubes) => {
  for (let i = 0; i < files.length; i++) {
    if (files[i].size > 3e7) {
      throw new Error("File Size Is To Big.");
    }
    const reader = new FileReader();
    reader.onload = function (e) {
      const toPr = e.target === null ? "0" : e.target.result;
      const image = new Image();
      image.src = toPr as string;
      image.onload = function (e) {
        console.log(e.target);
        total_cubes.total.set(
          files[i].name,
          Object.assign(
            {},
            {
              cubes: Math.ceil(
                ((e.target as HTMLImageElement).width *
                  (e.target as HTMLImageElement).height) /
                  AREA
              ),
              file: files[i],
              fileName: files[i].name,
            }
          )
        );
      };
    };
    reader.readAsDataURL(files[i]);
  }

  return 1;
};

//ADDS an element to tht dom tree
/* eslint-disable  @typescript-eslint/no-explicit-any */
export function ass_elem(
  elem_to_sel: string,
  elem_to_cr: string,
  text?: string,
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  style?: any,
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setAttr?: any
): HTMLElement {
  const elem = document.querySelector<HTMLElement>(elem_to_sel);
  if (elem === null) {
    console.error("There is not such element.");
    return {} as HTMLElement;
  }
  const new_elem = document.createElement(elem_to_cr);
  if (text) {
    const text_node = document.createTextNode(text);
    new_elem.appendChild(text_node);
  }
  if (style) {
    (new_elem as any).style.cssText = style;
  }
  if (setAttr) {
    for (const attr of setAttr.entries()) {
      new_elem.setAttribute(attr[0], attr[1]);
    }
  }
  elem.appendChild(new_elem);
  return new_elem;
}

export function ass_elemNS(
  elem_to_sel: string,
  elem_to_cr: string,
  nameSP: string,
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  style?: any,
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setAttr?: any
): Element {
  const elem = document.querySelector<HTMLElement>(elem_to_sel);
  if (elem === null) {
    console.error("There is not such element.");
    return {} as Element;
  }
  const new_elem = document.createElementNS(nameSP, elem_to_cr);
  elem.appendChild(new_elem);
  if (style) {
    (new_elem as any).style.cssText = style;
  }
  if (setAttr) {
    for (const attr of Object.entries(setAttr)) {
      new_elem.setAttribute(attr[0], attr[1] as string);
    }
  }
  return new_elem;
}

export const add_events = (
  elem: Element,
  events: string[],
  handler: (e: Event) => void
): void => {
  if (elem === null) {
    console.error("Elment Was Not Selected For Event.");
    return;
  }
  for (const ev of events) {
    elem.addEventListener(ev, handler);
  }
};
