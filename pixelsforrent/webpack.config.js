const path = require("path");
const { VueLoaderPlugin } = require("vue-loader");
const StyleLintPlugin = require("stylelint-webpack-plugin");
const { CheckerPlugin } = require("awesome-typescript-loader");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const ForkTsCheckerWebpackPlugin = require("fork-ts-checker-webpack-plugin");
const rootFolder = process.cwd();

const ext = {
  ts: /\.tsx?$/,
  js: /\.js$/,
  sass: /\.sass$/,
};
module.exports = {
  mode: "development",
  context: `${rootFolder}`,
  devtool:
    process.env.NODE_ENV === "development" ? "inline-source-map" : "source-map",
  entry: path.resolve(__dirname, "src/main.ts"),
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "pixels.js",
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
      {
        test: ext.ts,
        use: [
          {
            loader: "awesome-typescript-loader",
            options: {
              configFileName: `${rootFolder}/tsconfig.json`,
              forceIsolatedModules: true,
              useTranspileModule: true,
            },
          },
        ],
      },
      {
        enforce: "pre",
        test: ext.ts,
        loader: "source-map-loader",
      },
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.css$/i,
        use: [
          "style-loader",
          {
            loader: "css-loader",
            options: { importLoaders: 1 },
          },
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [
                  [
                    "autoprefixer",
                    {
                      // Options
                    },
                  ],
                ],
              },
            },
          },
        ],
      },
      {
        enforce: "pre",
        test: /\.(ts|js|vue)$/,
        loader: "eslint-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.scss$/,
        use: [
          "vue-style-loader",
          "css-loader",
          {
            loader: "sass-loader",
            options: {
              data: `
                              @import "@/scss/_variables.scss";
                              @import "@/scss/_mixins.scss";
                            `,
            },
          },
        ],
      },
      {
        test: /test\.js$/,
        use: "mocha-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.tsx?$/,
        use: [
          {
            loader: "ts-loader",
            options: {
              transpileOnly: true,
            },
          },
        ],
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    modules: ["node_modules"],
    extensions: [".tsx", ".ts", ".js", ".jsx", ".json", ".vue"],
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendors",
          chunks: "all",
        },
      },
    },
  },
  plugins: [
    new VueLoaderPlugin(),
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin(),
    new StyleLintPlugin({
      files: ["**/*.{vue,html,css,htm,scss,sass,ts, tsx}"],
    }),
    new CheckerPlugin(),
    new ForkTsCheckerWebpackPlugin(),
  ],

  devServer: {
    inline: true,
    hot: true,
    stats: "minimal",
    contentBase: __dirname,
    overlay: true,
    injectClient: false,
    disableHostCheck: true,
  },
};
