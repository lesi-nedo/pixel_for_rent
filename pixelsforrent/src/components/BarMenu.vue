<template>
  <div class="bar-menu bar-menuVar">
    <svg
      id="Home-button"
      clip-rule="evenodd"
      fill-rule="evenodd"
      stroke-linecap="round"
      stroke-linejoin="round"
      version="1.1"
      viewBox="98 98 193 193"
      xml:space="preserve"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <filter id="filter_Effect1">
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.0035 0.008"
            numOctaves="1"
            seed="2"
            stitchTiles="stitch"
            result="turbulence"
          >
            <animate
              attributeName="seed"
              values="1;3;5;7;9;11;13;15;17;19;21"
              dur="1.5s"
              repeatCount="indefinite"
            />
          </feTurbulence>
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.0035 0.007"
            numOctaves="1"
            seed="1"
            stitchTiles="stitch"
            result="turbulence1"
          />
          <feMerge result="merge">
            <feMergeNode in="turbulence1" result="mergeNode" />
            <feMergeNode in="turbulence" result="mergeNode1" />
          </feMerge>
          <feColorMatrix
            type="saturate"
            values="12"
            in="merge"
            result="colormatrix"
          />
          <feColorMatrix
            type="matrix"
            values="1 0 0 0 0
  0 1 0 0 0
  0 0 1 0 0
  0 0 0 10 0"
            in="colormatrix"
            result="colormatrix1"
          />
          <feDisplacementMap
            in="colormatrix1"
            in2="colormatrix"
            scale="40"
            xChannelSelector="R"
            yChannelSelector="G"
            result="displacementMap"
          />
          <feComposite
            in="displacementMap"
            in2="SourceAlpha"
            operator="in"
            result="composite1"
          />
        </filter>
        <linearGradient
          id="_E2"
          x1="135.91"
          x2="221.36"
          y1="212.98"
          y2="212.98"
          gradientTransform="matrix(1.3687 0 0 1.2524 -50.108 -64.523)"
          gradientUnits="userSpaceOnUse"
        >
          <stop offset=".47573" />
          <stop offset=".72087" />
        </linearGradient>
        <linearGradient
          id="_F2"
          x1="165.56"
          x2="196.93"
          y1="241.97"
          y2="213.86"
          gradientTransform="matrix(1 -2.8189e-18 2.8189e-18 1 18.598 -.02222)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#f00766" offset=".050971" />
          <stop stop-color="#a70337" offset=".8301" />
        </linearGradient>
        <linearGradient
          id="_G2"
          x1="112.53"
          x2="231.46"
          y1="166.18"
          y2="160.69"
          gradientTransform="matrix(.76551 -.64343 .64343 .76551 -80.004 146.96)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#7407f0" offset=".050971" />
          <stop stop-color="#a70337" offset=".8301" />
        </linearGradient>
        <radialGradient
          id="_H2"
          cx="112.53"
          cy="166.18"
          r="141.16"
          gradientTransform="matrix(-.71895 -.69506 .69506 -.71895 241.41 400.28)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#079ad6" offset="0" />
          <stop stop-color="#38e37e" offset=".91748" />
        </radialGradient>
      </defs>
      <g @click.stop="goToHome" class="Group_home">
        <g class="Group_EffectHome">
          <path
            d="m189.33 208.14h15.749c5.773 0 10.453 4.68 10.453 10.453l0.549 36.815h-11.002-15.749l-10.453-2e-3v-36.813c0-5.773 4.68-10.453 10.453-10.453z"
            filter="url(#filter_Effect1)"
          />
          <path
            d="m201.91 114.35c-0.165-0.021-6.9348-1.2126-21.801 9.3871-36.003 29.628-53.866 44.326-69.323 57.421-1.079 0.914-3.473 2.828-6.1 5.119-4.135 3.604-8.7635 8.496-9.1007 14.617-0.2069 3.755-0.0608 8.132 3.1752 12.545 5.4345 7.411 11.734 8.488 16.948 7.955 2.482-0.253 5.475-1.305 7.685-2.605 2.623-1.544 6.56-5.316 5.447-4.364-0.103 0.087 0.122 9.344 0.122 25.933 0 2.752 0.29 6.357-0.532 12.13-0.436 3.061-1.026 4.969-1.348 7.195-1.229 8.524-1.083 12.319 2.698 15.396 10.481 8.527 34.735 2.939 64.344 2.939 29.472 0 55.13 5.124 65.162-3.601 1.491-1.298 2.523-4.763 2.56-5.656 0.106-2.539 0.172-4.139-0.202-6.088-0.829-4.315-1.091-6.104-2.069-11.772-1.183-6.855-0.243-17.71-0.289-26.606-0.014-2.618 0.48-6.419 0-9.125-1.79-10.088 8.669 17.675 29.507 0.618 0.951-1.011 13.467-14.582-4.713-30.624-3.913-3.845-26.775-26.31-50.442-49.565-16.535-14.77-26.38-21.768-32.729-21.249z"
            filter="url(#filter_Effect1)"
          />
        </g>
        <g>
          <path
            d="m146.58 166.41c-5.172 4.733-8.371 11.27-8.371 18.492v54.319c0 7.221-5.172 18.364 0 23.097 5.172 4.732 20.688 3.054 28.581 3.054h55.197c7.893 0 23.409 1.678 28.581-3.054 5.172-4.733 0-15.876 0-23.097v-54.319c0-7.222-3.199-13.759-8.371-18.492-5.172-4.732-12.317-7.66-20.21-7.66h-55.197c-7.893 0-15.038 2.928-20.21 7.66z"
            fill="url(#_E2)"
          />
          <path
            d="m189.33 218.14h15.749c5.773 0 10.453 4.68 10.453 10.453l0.549 36.815h-26.751l-10.453-2e-3v-36.813c0-5.773 4.68-10.453 10.453-10.453z"
            fill="url(#_F2)"
          />
          <path
            d="m115 189.43s68-56.246 74.006-60.147c6.005-3.901 9.244-0.998 11.564 1.763l-3.717 10.293c5.633 6.701 4.766 16.7-1.935 22.333l-59.519 50.027c-6.702 5.633-16.701 4.767-22.334-1.935v0c-5.633-6.701-4.766-16.701 1.935-22.334z"
            fill="url(#_G2)"
          />
          <path
            d="m253.59 212.97s-54.705-53.802-64.493-64.195c-9.789-10.393-16.139-6.295-13.632-8.888l13.539-10.596c9.902-6.944 24.429 0.759 30.723 6.844l55.899 54.042c6.294 6.085 6.464 16.12 0.379 22.414v0c-6.085 6.294-16.121 6.464-22.415 0.379z"
            fill="url(#_H2)"
          />
        </g>
      </g>
    </svg>
    <svg
      id="Forum-button"
      clip-rule="evenodd"
      fill-rule="evenodd"
      stroke-linecap="round"
      stroke-linejoin="round"
      version="1.1"
      viewBox="790 300 685 685"
      xml:space="preserve"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <filter id="filter_Effect2">
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.0025 0.001"
            numOctaves="1"
            seed="2"
            stitchTiles="stitch"
            result="turbulence"
          >
            <animate
              attributeName="seed"
              values="1;3;5;7;9;11;13;15;17;19;21"
              dur="1.9s"
              repeatCount="indefinite"
            />
          </feTurbulence>
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.0015 0.004"
            numOctaves="1"
            seed="1"
            stitchTiles="stitch"
            result="turbulence1"
          />
          <feMerge result="merge">
            <feMergeNode in="turbulence1" result="mergeNode" />
            <feMergeNode in="turbulence" result="mergeNode1" />
          </feMerge>
          <feColorMatrix
            type="saturate"
            values="12"
            in="merge"
            result="colormatrix"
          />
          <feColorMatrix
            type="matrix"
            values="1 0 0 0 0
  0 1 0 0 0
  0 0 1 0 0
  120 0 0 10 0"
            in="colormatrix"
            result="colormatrix1"
          />
          <feDisplacementMap
            in="colormatrix1"
            in2="colormatrix"
            scale="40"
            xChannelSelector="R"
            yChannelSelector="G"
            result="displacementMap"
          />
          <feComposite
            in="displacementMap"
            in2="SourceAlpha"
            operator="in"
            result="composite1"
          />
        </filter>
        <radialGradient
          id="_M3"
          cx="979.16"
          cy="46.797"
          r="55.77"
          gradientTransform="matrix(13.448 0 0 12.72 -12387 116.92)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#7bfccf" offset=".41262" />
          <stop stop-color="#ad01cc" offset=".97816" />
        </radialGradient>
        <linearGradient
          id="_I3"
          x1="979.78"
          x2="1022.2"
          y1="25.232"
          y2="24.94"
          gradientTransform="matrix(13.865 0 0 14.301 -12755 97.124)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#013330" offset=".21602" />
          <stop stop-color="#160d0d" offset=".92718" />
        </linearGradient>
        <radialGradient
          id="_N3"
          cx="983"
          cy="25.357"
          r=".9483"
          gradientTransform="matrix(13.448 0 0 12.72 -12342 129.56)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#fc7b7b" offset=".41262" />
          <stop stop-color="#cc0101" offset="1" />
        </radialGradient>
        <radialGradient
          id="_O3"
          cx="983"
          cy="25.357"
          r=".9483"
          gradientTransform="matrix(13.448 0 0 12.72 -12307 129.75)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#fccc7b" offset=".41262" />
          <stop stop-color="#c6cc01" offset=".99272" />
        </radialGradient>
        <radialGradient
          id="_P3"
          cx="983"
          cy="25.357"
          r=".9483"
          gradientTransform="matrix(13.448 0 0 12.72 -12271 129.41)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#7bfc8d" offset=".41262" />
          <stop stop-color="#01cc88" offset=".9733" />
        </radialGradient>
        <linearGradient
          id="_J3"
          x1="974.99"
          x2="1023.1"
          y1="53.87"
          y2="53.87"
          gradientTransform="matrix(12.037 0 0 12.72 -10897 103.16)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#013330" offset=".21602" />
          <stop stop-color="#160d0d" offset=".92718" />
        </linearGradient>
        <linearGradient
          id="_K3"
          x1="860.44"
          x2="1036.4"
          y1="540.88"
          y2="660.34"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#490c0c" offset="0" />
          <stop stop-color="#c5048b" offset="1" />
        </linearGradient>
        <linearGradient
          id="_L3"
          x1="860.44"
          x2="1036.4"
          y1="540.88"
          y2="660.34"
          gradientTransform="matrix(-1 0 0 1 2253.8 111.25)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#0c2049" stop-opacity=".84596" offset="0" />
          <stop stop-color="#0f544c" offset="1" />
        </linearGradient>
      </defs>
      <g class="Group_forum">
        <g class="Group_EffectForum">
          <path
            d="m819.92 385.28h607.4c35.99-1.579 48.88 4.334 48.88 43.313l-0.9 351.1h53.23v58.198c0 28.978-27.85 58.199-58.79 58.199h-664.04c-30.934 0-58.79-29.221-58.79-58.199l1.029-58.198h42.038l-0.06-314.88c0-10.198-0.644-18.463 1.895-55.591 5.498-15.437 19.067-23.946 58.109-23.946z"
            filter="url(#filter_Effect2)"
          />
        </g>
        <g>
          <path
            d="m887.29 422.98h490.92c22.14 0 40.09 16.979 40.09 37.924v280.03c0 20.945-17.95 37.924-40.09 37.924h-490.92c-22.144 0-40.095-16.979-40.095-37.924v-280.03c0-20.945 17.951-37.924 40.095-37.924z"
            fill="url(#_M3)"
          />
          <path
            d="m877.05 422.98h511.4c16.49 0 29.85 13.788 29.85 30.797v27.426l-571.11-0.779v-26.647c0-17.009 13.368-30.797 29.858-30.797z"
            fill="url(#_I3)"
          />
          <path
            d="m875.7 441.69h3.514c6.073 0 10.996 4.656 10.996 10.4v0c0 5.744-4.923 10.401-10.996 10.401h-3.514c-6.073 0-10.996-4.657-10.996-10.401v0c0-5.744 4.923-10.4 10.996-10.4z"
            fill="url(#_N3)"
          />
          <path
            d="m910.25 441.87h3.514c6.073 0 10.996 4.657 10.996 10.401v0c0 5.744-4.923 10.4-10.996 10.4h-3.514c-6.073 0-10.996-4.656-10.996-10.4v0c0-5.744 4.923-10.401 10.996-10.401z"
            fill="url(#_O3)"
          />
          <path
            d="m946.82 441.54h3.514c6.073 0 10.996 4.656 10.996 10.4v0c0 5.744-4.923 10.401-10.996 10.401h-3.514c-6.073 0-10.997-4.657-10.997-10.401v0c0-5.744 4.924-10.4 10.997-10.4z"
            fill="url(#_P3)"
          />
          <path
            d="m812.76 742.05h640.26v50.957c0 28.143-21.59 50.957-48.22 50.957h-544.66c-26.632 0-48.221-22.814-48.221-50.957 0-28.142 0.844-50.957 0.844-50.957z"
            fill="url(#_J3)"
          />
          <path
            d="m927.7 499.1h211.5c17.3 0 19.36 83.561 2.06 83.561h-280.81s34.551-2.875 34.551-22.328c0-19.452 1.38-29.91 1.38-29.91 4.086-31.323 14.024-31.323 31.323-31.323z"
            fill="url(#_K3)"
          />
          <path
            d="m952.36 542.59c0-5.799 5.331-10.5 11.907-10.5s11.907 4.701 11.907 10.5c0 5.798-5.331 10.5-11.907 10.5s-11.907-4.702-11.907-10.5z"
            fill="#f7edf1"
          />
          <path
            d="m1012.6 542.59c0-5.799 5.33-10.5 11.9-10.5 6.58 0 11.91 4.701 11.91 10.5 0 5.798-5.33 10.5-11.91 10.5-6.57 0-11.9-4.702-11.9-10.5z"
            fill="#f7edf1"
          />
          <path
            d="m1075.1 542.59c0-5.799 5.33-10.5 11.91-10.5 6.57 0 11.9 4.701 11.9 10.5 0 5.798-5.33 10.5-11.9 10.5-6.58 0-11.91-4.702-11.91-10.5z"
            fill="#f7edf1"
          />
          <path
            d="m1326.1 610.35h-211.5c-17.3 0-19.37 83.56-2.07 83.56h280.83s-34.55-2.875-34.55-22.327c0-19.453-1.39-29.911-1.39-29.911-4.08-31.322-14.02-31.322-31.32-31.322z"
            fill="url(#_L3)"
          />
          <path
            d="m1301.4 653.84c0-5.799-5.33-10.5-11.9-10.5-6.58 0-11.91 4.701-11.91 10.5s5.33 10.5 11.91 10.5c6.57 0 11.9-4.701 11.9-10.5z"
            fill="#f7edf1"
          />
          <path
            d="m1241.2 653.84c0-5.799-5.33-10.5-11.91-10.5-6.57 0-11.9 4.701-11.9 10.5s5.33 10.5 11.9 10.5c6.58 0 11.91-4.701 11.91-10.5z"
            fill="#f7edf1"
          />
          <path
            d="m1178.7 653.84c0-5.799-5.33-10.5-11.91-10.5-6.57 0-11.91 4.701-11.91 10.5s5.34 10.5 11.91 10.5c6.58 0 11.91-4.701 11.91-10.5z"
            fill="#f7edf1"
          />
        </g>
      </g>
    </svg>
    <svg
      id="Blog-button"
      clip-rule="evenodd"
      fill-rule="evenodd"
      stroke-linecap="round"
      stroke-linejoin="round"
      version="1.1"
      viewBox="450 260 1400 1400"
      xml:space="preserve"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <linearGradient
          id="_F1"
          x1="458.01"
          x2="1761.8"
          y1="836.92"
          y2="835.57"
          gradientTransform="translate(55.812 4.0383)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#030d33" offset=".065534" />
          <stop stop-color="#061e1c" offset=".51214" />
          <stop stop-color="#04232b" offset=".95874" />
        </linearGradient>
        <linearGradient
          id="_E1"
          x1="436.63"
          x2="1038.3"
          y1="891.86"
          y2="986.19"
          gradientTransform="matrix(-.3474 .010886 .031321 .99951 1241.2 -53.966)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#17e57c" offset="0" />
          <stop stop-color="#06122d" offset=".89806" />
        </linearGradient>
        <linearGradient
          id="_D1"
          x1="1089.8"
          x2="1343.6"
          y1="716.7"
          y2="716.7"
          gradientTransform="translate(35.172 -4.3314)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#ca0a7c" offset="0" />
          <stop stop-color="#c4063c" offset="1" />
        </linearGradient>
        <linearGradient
          id="_C1"
          x1="1151.2"
          x2="1508.4"
          y1="1076.5"
          y2="1067.4"
          gradientTransform="translate(-89.195 -97.179)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#cbf300" offset="0" />
          <stop stop-color="#439105" offset=".94418" />
        </linearGradient>
        <linearGradient
          id="_B1"
          x1="959.22"
          x2="1659.4"
          y1="751.4"
          y2="743.86"
          gradientTransform="matrix(.99994 .01077 -.01077 .99994 -16.464 -52.451)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#030d33" offset=".065534" />
          <stop stop-color="#061e1c" offset=".51214" />
          <stop stop-color="#04232b" offset=".95874" />
        </linearGradient>
        <linearGradient
          id="_A1"
          x1="872.53"
          x2="1632.3"
          y1="991.12"
          y2="991.12"
          gradientTransform="matrix(1.2203 0 0 1.1922 -333.56 -213.29)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#030d33" offset=".065534" />
          <stop stop-color="#061e1c" offset=".51214" />
          <stop stop-color="#04232b" offset=".95874" />
        </linearGradient>
      </defs>
      <g class="Group_blog">
        <g class="Group_EffectBlog">
          <path
            d="M680.533+323.885L1643.11+323.885C1844.26+318.885+2013.01+503.951+2013.01+732.409L2013.01+952.562C2013.01+1178.02+1844.26+1368.09+1643.11+1368.09L695.583+1368.09C492.426+1368.09+323.682+1178.02+323.682+952.562L323.682+733.409C323.682+505.951+492.426+318.885+695.583+318.885Z"
            opacity="1"
            filter="url(#filter_Effect2)"
          />
        </g>

        <g>
          <path
            d="m807.59 421.41h716.22c162.25 0 333.77 131.52 333.77 333.77v171.57c0 162.24-131.52 333.77-333.77 333.77h-716.22c-162.24 0-333.77-131.53-333.77-333.77v-171.57c0-162.24 131.52-333.77 333.77-333.77z"
            fill="url(#_F1)"
          />
          <path
            d="m991.97 517.52s33.183 407.09 9.323 611.36l101.4-30.18c3.99-47.42 22.32-385.51 22.32-385.51 0-15.77-1.69-27.582-3.99-41.053-21.18-124.2-129.05-154.62-129.05-154.62z"
            fill="url(#_E1)"
          />
          <path
            d="m991.97 517.52c12.013-14.356 299.05 70.578 299.05 70.578 87.71 28.644 87.71 39.266 87.71 87.704v73.126c0 48.438-20.34 56.153-87.71 87.705l-144.54 65.955c-44.54 0-30.69-4.523-25.54-115.6 0.45-9.714 1.33-107.17 1.33-107.17 0-19.118-142.32-147.94-130.3-162.29z"
            fill="url(#_D1)"
          />
          <path
            d="m1149.8 865.75 252.07-24.785c48.44 0-19.7 64.052-19.7 112.49v51.678c0 48.44-39.27 87.7-87.7 87.7h-144.67c-48.44 0-56.25 29.09-45.55-33.76 0 0-43.74-46.23-42.15-105.62 1.59-59.385 39.26-87.705 87.7-87.705z"
            fill="url(#_C1)"
          />
          <path
            d="m1166.7 646.31 0.95 50.063c-0.32 29.6-10.61 94.508 18.99 94.827 0 0 104.12-1.948 126.07-10.312s10.01-95.431 2.79-124c-7.22-28.575-55.67-29.009-55.67-29.009l-37.84-0.408c-29.6-0.318-54.97-10.755-55.29 18.844z"
            fill="url(#_B1)"
          />
          <path
            d="m1192.1 902.59c95.92-9.147 124.67-5.029 159.28-20.89 67.81-31.068-24.91 57.294-24.91 92.584v15.739c0 35.291-29.28 63.901-65.41 63.901h-42.51c-36.12 0-106.81 26.18-84.71-19.31 0 0-13.09-19.09-22.1-54.643-14.66-57.903 15.9-71.234 80.36-77.381z"
            fill="url(#_A1)"
          />
        </g>
      </g>
    </svg>
    <svg
      id="Profile-button"
      clip-rule="evenodd"
      fill-rule="evenodd"
      stroke-linecap="round"
      stroke-linejoin="round"
      version="1.1"
      viewBox="750 100 615 645"
      xml:space="preserve"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <radialGradient
          id="_E4"
          cx="979.16"
          cy="46.797"
          r="55.77"
          gradientTransform="matrix(13.448 0 0 12.72 -12467 -116.29)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#7bfccf" offset=".41262" />
          <stop stop-color="#ad01cc" offset=".97816" />
        </radialGradient>
        <linearGradient
          id="_G4"
          x1="979.78"
          x2="1022.2"
          y1="25.232"
          y2="24.94"
          gradientTransform="matrix(13.865 0 0 14.301 -12835 -136.09)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#013330" offset=".21602" />
          <stop stop-color="#160d0d" offset=".92718" />
        </linearGradient>
        <radialGradient
          id="_D4"
          cx="983"
          cy="25.357"
          r=".9483"
          gradientTransform="matrix(13.448 0 0 12.72 -12422 -103.65)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#fc7b7b" offset=".41262" />
          <stop stop-color="#cc0101" offset="1" />
        </radialGradient>
        <radialGradient
          id="_C4"
          cx="983"
          cy="25.357"
          r=".9483"
          gradientTransform="matrix(13.448 0 0 12.72 -12387 -103.47)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#fccc7b" offset=".41262" />
          <stop stop-color="#c6cc01" offset=".99272" />
        </radialGradient>
        <radialGradient
          id="_B4"
          cx="983"
          cy="25.357"
          r=".9483"
          gradientTransform="matrix(13.448 0 0 12.72 -12350 -103.81)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#7bfc8d" offset=".41262" />
          <stop stop-color="#01cc88" offset=".9733" />
        </radialGradient>
        <radialGradient
          id="_A4"
          cx="995.66"
          cy="41.288"
          r="23.414"
          gradientTransform="matrix(11.428 0 0 10.903 -10470 -82.448)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#b6143b" offset="0" />
          <stop stop-color="#e60d52" offset=".59466" />
        </radialGradient>
        <linearGradient
          id="_F4"
          x1="974.99"
          x2="1023.1"
          y1="53.87"
          y2="53.87"
          gradientTransform="matrix(12.037 0 0 12.72 -10977 -130.05)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#013330" offset=".21602" />
          <stop stop-color="#160d0d" offset=".92718" />
        </linearGradient>
      </defs>
      <g class="Group_profile">
        <g class="Group_EffectProfile">
          <path
            d="m739.92 145.28h607.4c35.99-1.579 48.88 4.334 48.88 43.313l-0.9 351.1h53.23v58.198c0 28.978-27.85 58.199-58.79 58.199h-664.04c-30.934 0-58.79-29.221-58.79-58.199l1.029-58.198h42.038l-0.06-314.88c0-10.198-0.644-18.463 1.895-55.591 5.498-15.437 19.067-23.946 58.109-23.946z"
            filter="url(#filter_Effect2)"
          />
        </g>
        <g>
          <path
            d="m807.53 189.76h490.92c22.15 0 40.1 16.98 40.1 37.924v280.03c0 20.945-17.95 37.924-40.1 37.924h-490.92c-22.144 0-40.096-16.979-40.096-37.924v-280.03c0-20.944 17.952-37.924 40.096-37.924z"
            fill="url(#_E4)"
          />
          <path
            d="m797.29 189.76h511.4c16.49 0 29.86 13.789 29.86 30.797v27.426l-571.12-0.778v-26.648c0-17.008 13.368-30.797 29.859-30.797z"
            fill="url(#_G4)"
          />
          <path
            d="m795.94 208.48h3.514c6.073 0 10.996 4.657 10.996 10.401v0c0 5.744-4.923 10.4-10.996 10.4h-3.514c-6.073 0-10.996-4.656-10.996-10.4v0c0-5.744 4.923-10.401 10.996-10.401z"
            fill="url(#_D4)"
          />
          <path
            d="m830.49 208.66h3.515c6.072 0 10.996 4.656 10.996 10.4v0c0 5.744-4.924 10.401-10.996 10.401h-3.515c-6.073 0-10.996-4.657-10.996-10.401v0c0-5.744 4.923-10.4 10.996-10.4z"
            fill="url(#_C4)"
          />
          <path
            d="m867.06 208.32h3.514c6.073 0 10.996 4.657 10.996 10.401v0c0 5.744-4.923 10.4-10.996 10.4h-3.514c-6.073 0-10.996-4.656-10.996-10.4v0c0-5.744 4.923-10.401 10.996-10.401z"
            fill="url(#_B4)"
          />
          <path
            d="m792.31 367.71c0-59.276 51.725-107.33 115.53-107.33 63.807 0 115.53 48.053 115.53 107.33 0 59.277-51.727 107.33-115.53 107.33-63.808 0-115.53-48.053-115.53-107.33z"
            fill="url(#_A4)"
          />
          <path
            d="m900.72 409.2h16.299c34.167 0 36.547 15.779 39.553 26.34 4.906 17.237 5.082 25.421 5.082 25.421s-1.031 1.1-5.994 3.224c-3.907 1.672-10.228 4.088-20.564 6.355-4.047 0.888-10.699 2.281-20.01 2.757-4.905 0.252-10.555 0.094-16.936-0.19-16.012-0.713-32.57-7.162-32.57-7.162s-0.661-3.243-3.7-19.543c-5.814-31.181 16.729-37.202 38.84-37.202z"
            fill="#484154"
          />
          <path
            d="m906.67 324.07c24.583 0 44.512 17.412 44.512 38.892v19.184c0 21.479-19.929 38.892-44.512 38.892s-44.511-17.413-44.511-38.892v-19.184c0-21.48 19.928-38.892 44.511-38.892z"
            fill="#f7edf1"
          />
          <path
            d="m873.7 358.62c-4.696-0.546-4.023 7.796-11.542 4.341-0.754-0.346-1.349-4.956-1.758-6.139-1.302-3.766-1.793-12.678 1.758-17.289 4.794-6.226 2.676-8.731 5.835-13.225 3.158-4.494 6.313-7.935 8.344-9.088 1.901-1.079 4.466-2.308 7.677-3.409 3.211-1.1 7.067-2.072 11.552-2.635s9.597-0.718 15.319-0.186c5.723 0.533 12.055 1.754 18.979 3.942 1.288 0.407 1.794 0.872 1.791 1.369-3e-3 0.498-0.514 1.027-1.261 1.563-0.747 0.537-1.728 1.079-2.671 1.602s-1.847 1.026-2.439 1.484c-1.516 1.174-1.141 1.552 0.256 1.484 1.397-0.069 3.817-0.583 6.391-1.194 2.573-0.611 5.3-1.318 7.312-1.771 2.011-0.453 3.308-0.652 3.02-0.247-2.237 3.146-2.969 5.422-2.768 7.182s1.334 3.003 2.828 4.082 3.348 1.994 4.991 3.098c1.642 1.104 3.072 2.396 3.719 4.23 0.628 1.784 1.015 3.088 1.242 4.264 0.226 1.176 0.292 2.223 0.28 3.492-0.013 1.269-0.104 2.76-0.192 4.825s-0.173 4.703-0.173 8.265c0 0.243 7e-3 0.673-4e-3 1.171-0.01 0.498-0.038 1.064-0.105 1.582-0.068 0.518-0.176 0.986-0.347 1.289-0.172 0.302-0.407 0.438-0.729 0.289-0.322-0.148-5.729-3.13-12.726-6.765-6.996-3.636-5.683 1.628-22.258-10.689-5.731-4.258-24.34 2.822-30.847 4.932-6.508 2.11-6.196-0.714-11.474 8.151"
            fill="#544148"
          />
          <path
            d="m883.31 364.82c3.304 0 5.983 2.061 5.983 4.603v3.985c0 2.542-2.679 4.603-5.983 4.603-3.305 0-5.984-2.061-5.984-4.603v-3.985c0-2.542 2.679-4.603 5.984-4.603z"
            fill="#484154"
          />
          <path
            d="m933.32 365.8c3.305 0 5.983 2.061 5.983 4.603v3.985c0 2.542-2.678 4.603-5.983 4.603-3.304 0-5.983-2.061-5.983-4.603v-3.985c0-2.542 2.679-4.603 5.983-4.603z"
            fill="#484154"
          />
          <path
            d="m896.35 390.41h23.101c1.862 0 3.372 1.192 3.372 2.663 0 1.47-1.51 2.662-3.372 2.662h-23.101c-1.863 0-3.373-1.192-3.373-2.662 0-1.471 1.51-2.663 3.373-2.663z"
            fill="#484154"
          />
          <path
            d="m733 508.84h640.27v50.957c0 28.143-21.59 50.957-48.22 50.957h-544.67c-26.632 0-48.221-22.814-48.221-50.957s0.843-50.957 0.843-50.957z"
            fill="url(#_F4)"
          />
          <path
            d="m1100.5 272.41h210.05c2.61 0 4.73 2.118 4.73 4.731v0c0 2.613-2.12 4.731-4.73 4.731h-210.05c-2.62 0-4.73-2.118-4.73-4.731v0c0-2.613 2.11-4.731 4.73-4.731z"
            fill="#070707"
          />
          <path
            d="m1101.2 299.85h64.41c2.99 0 5.41 2.421 5.41 5.407v0c0 2.986-2.42 5.406-5.41 5.406h-64.41c-2.98 0-5.4-2.42-5.4-5.406v0c0-2.986 2.42-5.407 5.4-5.407z"
            fill="#070707"
          />
          <path
            d="m1210.9 299.85h36.02c2.99 0 5.41 2.421 5.41 5.407v0c0 2.986-2.42 5.406-5.41 5.406h-36.02c-2.99 0-5.41-2.42-5.41-5.406v0c0-2.986 2.42-5.407 5.41-5.407z"
            fill="#070707"
          />
          <path
            d="m1286.2 299.85h23.73c2.98 0 5.4 2.421 5.4 5.407v0c0 2.986-2.42 5.406-5.4 5.406h-23.73c-2.98 0-5.4-2.42-5.4-5.406v0c0-2.986 2.42-5.407 5.4-5.407z"
            fill="#070707"
          />
          <path
            d="m1101.1 329.18h63.29 56c2.67 0 4.84 2.164 4.84 4.834v1.146c0 2.669-2.17 4.833-4.84 4.833h-119.29c-2.67 0-4.84-2.164-4.84-4.833v-1.146c0-2.67 2.17-4.834 4.84-4.834z"
            fill="#070707"
          />
          <path
            d="m1252.8 329.82h61.33c2.6 0 4.7 2.106 4.7 4.704v1.405c0 2.598-2.1 4.704-4.7 4.704h-61.33c-2.59 0-4.7-2.106-4.7-4.704v-1.405c0-2.598 2.11-4.704 4.7-4.704z"
            fill="#070707"
          />
          <path
            d="m1101.8 359.39h210.05c2.62 0 4.73 2.118 4.73 4.731v0c0 2.613-2.11 4.731-4.73 4.731h-210.05c-2.62 0-4.73-2.118-4.73-4.731v0c0-2.613 2.11-4.731 4.73-4.731z"
            fill="#070707"
          />
        </g>
      </g>
    </svg>
    <svg
      id="ToRight-button"
      viewBox="900 545 594.2 594"
      xml:space="preserve"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <linearGradient
          id="_CN1"
          x1="374.35"
          x2="1971.5"
          y1="839.47"
          y2="839.47"
          gradientTransform="matrix(.60087 0 0 .59052 462.48 322.43)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#135858" offset="0" />
          <stop stop-color="#3a0a4c" offset=".93447" />
        </linearGradient>
        <linearGradient
          id="_BN1"
          x1="492.47"
          x2="1458.6"
          y1="934.62"
          y2="934.62"
          gradientTransform="matrix(.60087 0 0 .7642 485.44 93.126)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#00f3cb" offset="0" />
          <stop stop-color="#00da8b" offset=".97573" />
        </linearGradient>
        <linearGradient
          id="_AN1"
          x1="1269"
          x2="1883.1"
          y1="836.56"
          y2="828.18"
          gradientTransform="matrix(.519 0 0 .48265 405.16 405.5)"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#e2166c" offset="0" />
          <stop stop-color="#cb0961" offset=".9733" />
        </linearGradient>
      </defs>
      <g @mousedown.stop="toRight" class="Group_ToRight">
        <g class="Group_EffectToRight">
          <path
            d="m848.83 454.14h639.2c137.8 0 249.51 127.83 249.51 285.52v151.43c0 157.69-111.71 285.52-249.51 285.52h-639.2c-137.8 0-249.52-127.83-249.52-285.52v-151.43c0-157.69 111.71-285.52 249.52-285.52z"
            filter="url(#filter_Effect2)"
          />
        </g>
        <g>
          <path
            d="m897.79 532.88h538.93c116.19 0 210.38 100.95 210.38 225.48v119.59c0 124.53-94.19 225.48-210.38 225.48h-538.93c-116.19 0-210.38-100.95-210.38-225.48v-119.59c0-124.53 94.189-225.48 210.38-225.48z"
            fill="url(#_CN1)"
          />
          <path
            d="m811.88 734.65h519.48c16.87 0 30.54 17.384 30.54 38.83v67.771c0 21.446-13.67 38.831-30.54 38.831h-519.48c-16.862 0-30.531-17.385-30.531-38.831v-67.771c0-21.446 13.669-38.83 30.531-38.83z"
            fill="url(#_BN1)"
          />
          <path
            d="m1090.1 660.52h252.43c24.57 0 181.59 134.16 181.59 147.7 0 13.545-167.02 149.8-181.59 149.8h-252.43c-14.56 0 137.79-136.26 137.79-149.8 0-13.544-152.35-147.7-137.79-147.7z"
            fill="url(#_AN1)"
          />
        </g>
      </g>
    </svg>

    <svg
      id="Donate-button"
      height="100%"
      style="
        fill-rule: evenodd;
        clip-rule: evenodd;
        stroke-linecap: round;
        stroke-linejoin: round;
      "
      xmlns:xlink="http://www.w3.org/1999/xlink"
      xmlns="http://www.w3.org/2000/svg"
      xml:space="preserve"
      width="100%"
      version="1.1"
      viewBox="400 150 1250 830"
    >
      <defs>
        <linearGradient
          y1="541.426"
          id="LinearGradient"
          x1="483.841"
          y2="541.426"
          x2="1643.25"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1.01283 0 -2.5321)"
        >
          <stop stop-color="#6300ba" offset="0.00970874" />
          <stop stop-color="#87095d" offset="0.398058" />
          <stop stop-color="#0d7f95" offset="0.73301" />
          <stop stop-color="#124ba7" offset="0.990291" />
        </linearGradient>
        <radialGradient
          cx="775.673"
          r="767.848"
          id="_BD1"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1 7.77108 7.80808)"
          cy="540"
        >
          <stop stop-color="#ee0665" offset="0.0509709" />
          <stop stop-color="#c2009c" offset="1" />
        </radialGradient>
        <radialGradient
          cx="775.673"
          r="767.848"
          id="_BD2"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1 7.77108 7.80808)"
          cy="540"
        >
          <stop stop-color="#ee0665" offset="0.0509709" />
          <stop stop-color="#c2009c" offset="1" />
        </radialGradient>
        <radialGradient
          cx="775.673"
          r="767.848"
          id="_BD3"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1 7.77108 7.80808)"
          cy="540"
        >
          <stop stop-color="#ee0665" offset="0.0509709" />
          <stop stop-color="#c2009c" offset="1" />
        </radialGradient>
        <radialGradient
          cx="775.673"
          r="767.848"
          id="_BD4"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1 7.77108 7.80808)"
          cy="540"
        >
          <stop stop-color="#ee0665" offset="0.0509709" />
          <stop stop-color="#c2009c" offset="1" />
        </radialGradient>
        <radialGradient
          cx="775.673"
          r="767.848"
          id="_BD5"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1 7.77108 7.80808)"
          cy="540"
        >
          <stop stop-color="#ee0665" offset="0.0509709" />
          <stop stop-color="#c2009c" offset="1" />
        </radialGradient>
        <radialGradient
          cx="775.673"
          r="767.848"
          id="_BD6"
          gradientUnits="userSpaceOnUse"
          gradientTransform="matrix(1 0 0 1 7.77108 7.80808)"
          cy="540"
        >
          <stop stop-color="#ee0665" offset="0.0509709" />
          <stop stop-color="#c2009c" offset="1" />
        </radialGradient>
      </defs>
      <g class="Group_Donate">
        <g class="Group_EffectDonate">
          <path
            d="M686.36+108.359L1441.32+108.359C1604.08+108.359+1736.03+263.984+1736.03+455.958L1736.03+640.312C1736.03+832.286+1604.08+987.911+1441.32+987.911L686.36+987.911C523.598+987.911+391.653+832.286+391.653+640.312L391.653+455.958C391.653+263.984+523.598+108.359+686.36+108.359Z"
            opacity="1"
            filter="url(#filter_Effect2)"
          />
        </g>
        <g>
          <path
            d="M738.001+197.322L1389.09+197.322C1529.46+197.322+1643.25+320.654+1643.25+472.792L1643.25+618.892C1643.25+771.03+1529.46+894.362+1389.09+894.362L738.001+894.362C597.633+894.362+483.841+771.03+483.841+618.892L483.841+472.792C483.841+320.654+597.633+197.322+738.001+197.322Z"
            fill="url(#_BD1)"
          />
          <path
            d="M763.337+236.998L1363.74+236.998C1493.18+236.998+1598.11+346.031+1598.11+480.529L1598.11+609.689C1598.11+744.187+1493.18+853.22+1363.74+853.22L763.337+853.22C633.897+853.22+528.965+744.187+528.965+609.689L528.965+480.529C528.965+346.031+633.897+236.998+763.337+236.998Z"
            fill="#fff"
          />
          <path
            d="M665.346+663.292L665.346+388.46L723.632+388.46C746.277+388.46+763.454+394.636+775.163+406.988C786.872+419.34+792.726+436.839+792.726+459.484L792.726+588.022C792.726+613.755+786.486+632.734+774.005+644.957C761.524+657.18+743.575+663.292+720.158+663.292L665.346+663.292ZM704.718+425.516L704.718+626.236L722.86+626.236C733.925+626.236+741.774+623.47+746.406+617.937C751.038+612.404+753.354+603.719+753.354+591.882L753.354+459.484C753.354+448.676+751.167+440.313+746.792+434.394C742.417+428.475+734.44+425.516+722.86+425.516L704.718+425.516Z"
            opacity="1"
            fill="url(#_BD1)"
          />
          <path
            d="M812.738+453.308C812.738+442.243+814.668+432.464+818.528+423.972C822.388+415.48+827.535+408.403+833.968+402.742C840.144+397.338+847.156+393.221+855.005+390.39C862.854+387.559+870.767+386.144+878.744+386.144C886.721+386.144+894.634+387.559+902.483+390.39C910.332+393.221+917.473+397.338+923.906+402.742C930.082+408.403+935.1+415.48+938.96+423.972C942.82+432.464+944.75+442.243+944.75+453.308L944.75+598.444C944.75+610.024+942.82+619.931+938.96+628.166C935.1+636.401+930.082+643.22+923.906+648.624C917.473+654.285+910.332+658.531+902.483+661.362C894.634+664.193+886.721+665.608+878.744+665.608C870.767+665.608+862.854+664.193+855.005+661.362C847.156+658.531+840.144+654.285+833.968+648.624C827.535+643.22+822.388+636.401+818.528+628.166C814.668+619.931+812.738+610.024+812.738+598.444L812.738+453.308ZM852.11+598.444C852.11+607.965+854.748+614.978+860.023+619.481C865.298+623.984+871.539+626.236+878.744+626.236C885.949+626.236+892.19+623.984+897.465+619.481C902.74+614.978+905.378+607.965+905.378+598.444L905.378+453.308C905.378+443.787+902.74+436.774+897.465+432.271C892.19+427.768+885.949+425.516+878.744+425.516C871.539+425.516+865.298+427.768+860.023+432.271C854.748+436.774+852.11+443.787+852.11+453.308L852.11+598.444Z"
            opacity="1"
            fill="url(#_BD2)"
          />
          <path
            d="M963.218+663.292L963.218+388.46L1001.05+388.46L1060.49+554.054L1061.26+554.054L1061.26+388.46L1100.63+388.46L1100.63+663.292L1063.58+663.292L1003.36+498.084L1002.59+498.084L1002.59+663.292L963.218+663.292Z"
            opacity="1"
            fill="url(#_BD3)"
          />
          <path
            d="M1200.93+567.178L1181.63+467.59L1180.86+467.59L1161.56+567.178L1200.93+567.178ZM1103.66+663.292L1165.04+388.46L1197.85+388.46L1259.22+663.292L1219.85+663.292L1208.27+604.234L1154.61+604.234L1143.03+663.292L1103.66+663.292Z"
            opacity="1"
            fill="url(#_BD4)"
          />
          <path
            d="M1268.42+663.292L1268.42+425.516L1222.88+425.516L1222.88+388.46L1353.34+388.46L1353.34+425.516L1307.8+425.516L1307.8+663.292L1268.42+663.292Z"
            opacity="1"
            fill="url(#_BD5)"
          />
          <path
            d="M1355.99+663.292L1355.99+388.46L1473.33+388.46L1473.33+425.516L1395.36+425.516L1395.36+506.19L1463.29+506.19L1463.29+543.246L1395.36+543.246L1395.36+623.92L1473.33+623.92L1473.33+663.292L1355.99+663.292Z"
            opacity="1"
            fill="url(#_BD6)"
          />
        </g>
      </g>
    </svg>
  </div>
</template>

<script lang="ts">
import { defineComponent, onBeforeMount } from "vue";
import { toRightMenu } from "./functions";
import { useRouter } from "vue-router";
export default defineComponent({
  name: "BarMenu",
  setup() {
    const router = useRouter();
    const goToHome = () => {
      router.push({ path: "/home" });
      if (router.currentRoute.value.fullPath == "/home") router.go(0);
    };
    onBeforeMount(() => {
      router.push({ path: "/home" });
    });
    return { goToHome };
  },
  data() {
    let view = window.matchMedia("(max-width: 600px)");
    return {
      //true Left false right
      barClick: {
        view,
        match: view.matches,
        position:
          localStorage.getItem("_PosBar") != null
            ? !(localStorage.getItem("_PosBar") === "true")
            : true,
      },
    };
  },
  mounted() {
    let view = window.matchMedia("(max-width: 600px)");
    const localPos = localStorage.getItem("_PosBar");
    if (localPos != null) {
      toRightMenu(localPos === "true", this.$el, view.matches, 0);
    }
  },
  methods: {
    async toRight() {
      let direc = 0;
      const path = ["/nedo*", "/blog*", "/profile*", "/donate*"];
      for (let i = 0; i < 3; i++) {
        if (
          new RegExp(path[i]).test(this.$router.currentRoute.value.fullPath)
        ) {
          direc = i;
          break;
        }
      }
      await new Promise((resolve) => {
        setTimeout(() => {
          resolve(
            toRightMenu(
              this.barClick.position,
              this.$el,
              this.barClick.view.matches,
              direc
            )
          );
        }, 100);
      });
      this.barClick.position = !this.barClick.position;
    },
  },
});
</script>

<style lang="scss">
$widthRadius: 2px;
//REMEMBER ORDER COUNTS

.lineSv {
  display: none;
  position: relative;
  top: 90px;
  left: -38px;
  height: 500px;
  z-index: 4;
}
.bar-menuVar {
  --barPositionLeft: 0;
  --PEMunuBar: 9.105vmin;
  --barPosSmall: 15.1vmin;
}
.bar-menu {
  display: block;
  user-select: none;
  position: fixed;
  width: 9%;
  width: 9.1vmin;
  height: 100%;
  margin-bottom: auto;
  border-radius: $widthRadius;
  background-color: #e3dededb;
  right: 0;
  left: var(--barPositionLeft);
  bottom: 0px;
  z-index: 100 !important;
}
.bar-menu:after {
  position: absolute;
  display: block;
  content: "";
  height: 100%;
  width: 1vmin;
  right: 0%;
  left: 9%;
  left: var(--PEMunuBar);
  bottom: 0px;
  top: 0px;
  background: linear-gradient(
    320deg,
    #f56e00,
    #a300cc,
    #098bc3ab,
    #b1023c,
    #25e9cc,
    #02b18e96 120%
  );
  border-radius: 2px;
  animation: animGrad 4s $randCubicBezBarMen alternate infinite;
  animation-fill-mode: forwards;
  animation-delay: 0s;
  background-size: 200% 200%;
  z-index: 999 !important;
}
@keyframes animGrad {
  0% {
    background-position: $size-border1 10%;
  }
  30% {
    background-position: 0% $size-border2;
  }
  50% {
    background-position: $size-border4 $size-border3;
  }
  75% {
    background-position: $size-border5 30%;
  }
  100% {
    background-position: $size-border6 90%;
  }
}

#Home-button {
  overflow: visible;
  display: block;
  position: absolute;
  z-index: 999 !important;
  left: -2%;
  width: 100%;
  width: 9.3vmin;
  height: 7%;
  top: $TopPosBar + 3%;
  padding: 0;
  margin: 0;
}

#Forum-button {
  overflow: visible;
  display: block;
  position: absolute;
  align-items: center;
  left: 0;
  width: 100%;
  width: 9vmin;
  height: 6%;
  top: $TopPosBar + 14%;
  padding: 0;
  margin: 0;
  flex-shrink: 0;
  flex-grow: 0;
  z-index: 999 !important;
}

#Blog-button {
  display: block;
  overflow: visible;
  position: absolute;
  left: 0%;
  width: 100%;
  width: 9vmin;
  height: 6%;
  top: $TopPosBar + 24%;
  padding: 0;
  margin: 0;
  z-index: 999 !important;
}

#Profile-button {
  display: block;
  position: absolute;
  overflow: visible;
  left: 2%;
  width: 100%;
  width: 8.8vmin;
  height: 6%;
  top: $TopPosBar + 34%;
  padding: 0;
  margin: 0;
  z-index: 999 !important;
}

#ToRight-button {
  display: block;
  position: absolute;
  overflow: visible;
  left: 20%;
  width: 70%;
  width: 5.8vmin;
  height: 3.8%;
  top: $TopPosBar - 19%;
  padding: 0;
  margin: 0;
  z-index: 999 !important;
}

#Donate-button {
  display: block;
  position: absolute;
  overflow: visible;
  left: 10%;
  width: 67%;
  width: 7vmin;
  height: 5%;
  top: $TopPosBar + 60%;
  padding: 0;
  margin: 0;
  z-index: 999 !important;
}

@media screen and (max-width: 600px) {
  //Do Not TOuch: ORDER COUNTS: WATCH toRight FUNCTION!!!
  .bar-menu {
    width: 15%;
    width: 15.1vmin;
  }
  .bar-menu:after {
    left: var(--barPosSmall);
  }
  #Home-button {
    overflow: visible;
    left: 13%;
    width: 100%;
    width: 12.5vmin;
    height: 10.5%;
    top: $TopPosBar + 5%;
  }
  #Forum-button {
    left: 20%;
    width: 100%;
    width: 10.5vmin;
    height: 8.5%;
    top: $TopPosBar + 17%;
  }

  #Blog-button {
    left: 18%;
    width: 100%;
    width: 10.5vmin;
    height: 8.5%;
    top: $TopPosBar + 27%;
  }
  #Profile-button {
    left: 18%;
    width: 100%;
    width: 10.5vmin;
    height: 8.5%;
    top: $TopPosBar + 37%;
  }
  #ToRight-button {
    left: 30%;
    width: 100%;
    width: 7vmin;
    height: 6.3%;
    top: 3%;
  }
  #Donate-button {
    left: 10%;
    width: 140%;
    width: 12.5vmin;
    height: 11%;
    top: 78%;
  }
}

.Group_EffectHome,
.Group_EffectForum,
.Group_EffectProfile,
.Group_EffectBlog,
.Group_EffectToRight,
.Group_EffectDonate {
  opacity: 0;
}

.Group_forum:active,
.Group_profile:active,
.Group_blog:active,
.Group_ToRight:active,
.Group_Donate:active {
  animation: fadeAll 0.15s cubic-bezier(0.0075, 0.07, 0.105, 0.1);
}

.Group_home:active {
  animation: fadeHome 0.15s cubic-bezier(0.0075, 0.07, 0.105, 0.1);
}

.Group_home:hover g[class="Group_EffectHome"],
.Group_forum:hover g[class="Group_EffectForum"],
.Group_profile:hover g[class="Group_EffectProfile"],
.Group_blog:hover g[class="Group_EffectBlog"],
.Group_ToRight:hover g[class="Group_EffectToRight"],
.Group_Donate:hover g[class^="Group_EffectDonate"] {
  animation: appear 1s $randCubicBezBarHome;
  animation-fill-mode: forwards;
}

.Group_Donate g[class="Group_EffectDonate selected_to_pay"] {
  animation: appear 1s $randCubicBezBarHome;
  animation-fill-mode: forwards;
}

@keyframes fadeHome {
  0% {
    opacity: 1;
  }
  70% {
    transform: matrix(0.7, 0.0095, 0.000006, 0.7, 20, 0);
    opacity: 0.5;
  }
  75% {
    transform: matrix(1.13, 0, 0, 1.13, 0, 0);
    opacity: 0.7;
  }
  80% {
    transform: matrix(1.09, 0, 0, 1.09, 0, 0);
    opacity: 0.9;
  }
  85% {
    transform: matrix(1.1, 0, 0, 1.1, 0, 0);
    opacity: 1;
  }
}

@keyframes fadeAll {
  0% {
    opacity: 1;
  }
  70% {
    transform: matrix(0.7, 0.0095, 0.000006, 0.7, 200, 0);
    opacity: 0.5;
  }
  75% {
    transform: matrix(1.13, 0, 0, 1.13, 0, 0);
    opacity: 0.7;
  }
  80% {
    transform: matrix(1.09, 0, 0, 1.09, 0, 0);
    opacity: 0.9;
  }
  85% {
    transform: matrix(1.1, 0, 0, 1.1, 0, 0);
    opacity: 1;
  }
}

@keyframes appear {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
