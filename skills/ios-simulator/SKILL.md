---
name: ios-simulator
description: iOS application testing and debugging using Xcode simulators for development and QA workflows
---

# iOS Simulator Skill

Test and debug iOS applications using Xcode simulators without physical devices.

## When to Use
- iOS app testing
- UI/UX validation
- Debugging iOS issues
- Automated testing setup

## Core Capabilities
- Launch simulators for different iOS versions
- Install and test apps
- Capture screenshots and recordings
- Simulate device conditions (network, location, etc.)
- Automated testing with XCTest
- Accessibility inspector

## Key Commands
```bash
# List available simulators
xcrun simctl list

# Boot simulator
xcrun simctl boot "iPhone 14"

# Install app
xcrun simctl install booted /path/to/app.app

# Launch app
xcrun simctl launch booted com.example.app

# Screenshot
xcrun simctl io booted screenshot screenshot.png

# Record video
xcrun simctl io booted recordVideo video.mp4
```

## Best Practices
- Test on multiple iOS versions
- Use device-specific simulators
- Leverage accessibility inspector
- Automate with XCUITest

## Resources
- Xcode Documentation: https://developer.apple.com/documentation/xcode
- simctl reference: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/iOS_Simulator_Guide/
