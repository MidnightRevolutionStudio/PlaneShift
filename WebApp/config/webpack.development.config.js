const ForkTsCheckerWebpackPlugin = require("fork-ts-checker-webpack-plugin");
const DashboardPlugin = require("webpack-dashboard/plugin");
const webpack = require("webpack");
const path = require("path");
const CleanWebpackPlugin = require("clean-webpack-plugin").default;
const copyWebpack = require("copy-webpack-plugin");

const DISTRIBUTION_PATH = "../dist";

module.exports = () => ({
  devtool: "source-map",
  plugins: [
    new DashboardPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new CleanWebpackPlugin(),
    new ForkTsCheckerWebpackPlugin({
      tslint: path.resolve(__dirname, "../tslint.json")
    }),
    new copyWebpack([
      {
        from: path.resolve(__dirname, "../devconfig/config.json"),
        to: path.resolve(__dirname, DISTRIBUTION_PATH)
      }
    ])
  ]
});
