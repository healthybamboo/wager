/**
 * @jest-environment jsdom
 */
import { render,screen } from "@testing-library/react"
import React from "react"
import {test, expect} from "@jest/globals"
import  App  from "../../src/tsx/App"

test("タスクの追加と一覧表示", () => {
  render(<App />)
  const h1 = screen.getByTestId("app-test").textContent

  expect(h1).toMatch(/App/)

})