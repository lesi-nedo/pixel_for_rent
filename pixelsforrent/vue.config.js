module.exports = {
  publicPath: "/",
  outputDir: "dist",
  lintOnSave: "error",
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "pixelsForRent";
      return args;
    });
  },
  css: {
    loaderOptions: {
      sass: {
        additionalData: `@import "@/styles/_variabels.scss";`,
      },
    },
  },
};
