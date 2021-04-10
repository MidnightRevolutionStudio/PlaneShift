const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const WebpackMd5Hash = require("webpack-md5-hash");
const createStyledComponentsTransformer = require("typescript-plugin-styled-components")
  .default;
const styledComponentsTransformer = createStyledComponentsTransformer();
const webpackMerge = require("webpack-merge");
const copyWebpack = require("copy-webpack-plugin");

const modeConfig = (env) => {
  return require(`./webpack.${env}.config.js`)(env);
};

const DISTRIBUTION_PATH = "../dist";

module.exports = ({ mode } = { mode: "development" }) => {
  return webpackMerge(
    {
      context: path.resolve(__dirname, "../"),
      // @ts-ignore
      mode,
      entry: { main: "./src/index.tsx" },
      optimization: {
        splitChunks: { name: "dependencies", chunks: "initial" }
      },
      devServer: {
        contentBase: path.resolve(__dirname, DISTRIBUTION_PATH),
        historyApiFallback: true
      },
      module: {
        rules: [
          {
            test: /\.tsx?$/,
            use: {
              loader: "ts-loader",
              options: {
                transpileOnly: true,
                getCustomTransformers: () => ({
                  before: [styledComponentsTransformer]
                })
              }
            },
            exclude: /node_modules/
          },
          {
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
          }
        ]
      },
      resolve: {
        extensions: [".tsx", ".ts", ".js", ".jsx"],
        modules: [
          path.resolve(__dirname, "../src"),
          path.resolve(__dirname, "../node_modules")
        ]
      },
      output: {
        path: path.resolve(__dirname, DISTRIBUTION_PATH),
        publicPath: "/",
        filename: "[name].[hash].js"
      },
      plugins: [
        new WebpackMd5Hash(),
        new HtmlWebpackPlugin({
          inject: "body",
          hash: true,
          template: "./src/index.html",
          filename: "index.html",
          favicon: "./src/images/favicon.png"
        }),
        new copyWebpack([
          {
            from: path.resolve(__dirname, "../hostconfig/web.config"),
            to: path.resolve(__dirname, DISTRIBUTION_PATH)
          },
          {
            from: path.resolve(
              __dirname,
              "../hostconfig/ContextHierarchy.json"
            ),
            to: path.resolve(__dirname, DISTRIBUTION_PATH)
          }
        ])
      ]
    },
    modeConfig(mode)
  );
};
