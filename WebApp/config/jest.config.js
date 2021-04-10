module.exports = {
  moduleFileExtensions: ["ts", "tsx", "js"],
  testURL: "http://localhost",
  rootDir: "../",
  preset: "ts-jest",
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>src/setupTests.js"],
  clearMocks: true,
  transform: {
    "^.+\\.(ts|tsx|js)$": "ts-jest"
  },
  globals: {
    "ts-jest": {
      tsConfig: "tsconfig.json",
      diagnostics: false
    }
  },
  moduleNameMapper: {
    "\\.(css|less)$": "identity-obj-proxy"
  },
  testPathIgnorePatterns: ["/node_modules/", "/helpers/"],
  moduleDirectories: ["node_modules", "src"],
  collectCoverage: false,
  collectCoverageFrom: ["src/**/*.{ts,tsx}", "!src/__tests__/**/*"]
};
