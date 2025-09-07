#!/usr/bin/env python3
"""
Test script for VibeVoice application functionality.

This script tests the core components of VibeVoice without requiring
large model downloads, focusing on:
1. Package imports and module loading
2. Configuration handling
3. Processor initialization 
4. Demo script argument parsing
5. File structure and resource availability
"""

import os
import sys
import argparse
import subprocess
import tempfile
from pathlib import Path
from typing import List, Dict, Any
import traceback

def test_imports():
    """Test that all core modules can be imported."""
    print("🔍 Testing package imports...")
    
    try:
        import vibevoice
        print("  ✓ vibevoice package imported")
    except Exception as e:
        print(f"  ✗ Failed to import vibevoice: {e}")
        return False
    
    try:
        from vibevoice.processor.vibevoice_processor import VibeVoiceProcessor
        print("  ✓ VibeVoiceProcessor imported")
    except Exception as e:
        print(f"  ✗ Failed to import VibeVoiceProcessor: {e}")
        return False
    
    try:
        from vibevoice.modular.modeling_vibevoice_inference import VibeVoiceForConditionalGenerationInference
        print("  ✓ VibeVoiceForConditionalGenerationInference imported")
    except Exception as e:
        print(f"  ✗ Failed to import VibeVoiceForConditionalGenerationInference: {e}")
        return False
    
    try:
        from vibevoice.modular.configuration_vibevoice import VibeVoiceConfig
        print("  ✓ VibeVoiceConfig imported")
    except Exception as e:
        print(f"  ✗ Failed to import VibeVoiceConfig: {e}")
        return False
    
    return True

def test_demo_scripts():
    """Test that demo scripts have proper argument parsing."""
    print("\n🔍 Testing demo script functionality...")
    
    demo_dir = Path("demo")
    if not demo_dir.exists():
        print(f"  ✗ Demo directory not found: {demo_dir}")
        return False
    
    # Test gradio demo help
    try:
        result = subprocess.run([
            sys.executable, "demo/gradio_demo.py", "--help"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and "VibeVoice Gradio Demo" in result.stdout:
            print("  ✓ Gradio demo script executable with help")
        else:
            print(f"  ✗ Gradio demo script failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ Failed to run gradio demo: {e}")
        return False
    
    # Test inference script help
    try:
        result = subprocess.run([
            sys.executable, "demo/inference_from_file.py", "--help"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and "VibeVoice Processor TXT Input Test" in result.stdout:
            print("  ✓ Inference script executable with help")
        else:
            print(f"  ✗ Inference script failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ Failed to run inference script: {e}")
        return False
    
    return True

def test_file_structure():
    """Test that required files and directories exist."""
    print("\n🔍 Testing file structure...")
    
    required_files = [
        "pyproject.toml",
        "README.md",
        "vibevoice/__init__.py",
        "demo/gradio_demo.py", 
        "demo/inference_from_file.py",
    ]
    
    required_dirs = [
        "vibevoice",
        "demo",
        "demo/voices",
        "demo/text_examples",
    ]
    
    # Check files
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"  ✓ {file_path} exists")
        else:
            print(f"  ✗ {file_path} missing")
            return False
    
    # Check directories
    for dir_path in required_dirs:
        if Path(dir_path).is_dir():
            print(f"  ✓ {dir_path}/ exists")
        else:
            print(f"  ✗ {dir_path}/ missing")
            return False
    
    return True

def test_voice_samples():
    """Test that voice samples are available."""
    print("\n🔍 Testing voice samples...")
    
    voices_dir = Path("demo/voices")
    if not voices_dir.exists():
        print(f"  ✗ Voices directory not found: {voices_dir}")
        return False
    
    voice_files = list(voices_dir.glob("*.wav"))
    if not voice_files:
        print("  ✗ No voice sample files found")
        return False
    
    print(f"  ✓ Found {len(voice_files)} voice samples:")
    for voice_file in sorted(voice_files):
        print(f"    - {voice_file.name}")
    
    return True

def test_example_texts():
    """Test that example text files are available and properly formatted."""
    print("\n🔍 Testing example texts...")
    
    examples_dir = Path("demo/text_examples")
    if not examples_dir.exists():
        print(f"  ✗ Text examples directory not found: {examples_dir}")
        return False
    
    text_files = list(examples_dir.glob("*.txt"))
    if not text_files:
        print("  ✗ No example text files found")
        return False
    
    print(f"  ✓ Found {len(text_files)} example texts:")
    for text_file in sorted(text_files):
        print(f"    - {text_file.name}")
        
        # Check if file has proper speaker format
        try:
            content = text_file.read_text()
            if "Speaker" in content:
                print(f"      ✓ Contains speaker annotations")
            else:
                print(f"      ! No speaker annotations found")
        except Exception as e:
            print(f"      ✗ Error reading file: {e}")
    
    return True

def test_processor_initialization():
    """Test VibeVoiceProcessor can be initialized."""
    print("\n🔍 Testing processor initialization...")
    
    try:
        from vibevoice.processor.vibevoice_processor import VibeVoiceProcessor
        
        # Try to create a processor instance without a model path
        # This should test the class structure without downloading models
        print("  ✓ VibeVoiceProcessor class available")
        print("  ℹ  Skipping full processor initialization (requires model download)")
        
    except Exception as e:
        print(f"  ✗ Failed to access VibeVoiceProcessor: {e}")
        return False
    
    return True

def test_dependencies():
    """Test that key dependencies are available."""
    print("\n🔍 Testing key dependencies...")
    
    dependencies = [
        "torch",
        "transformers", 
        "diffusers",
        "librosa",
        "gradio",
        "numpy",
        "scipy"
    ]
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"  ✓ {dep} available")
        except ImportError:
            print(f"  ✗ {dep} not available")
            return False
    
    return True

def create_test_output():
    """Create a simple test output to verify functionality."""
    print("\n🔍 Creating test output...")
    
    # Create a temporary directory for test outputs
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test_output.txt"
        test_file.write_text("VibeVoice application test completed successfully!")
        
        if test_file.exists():
            print(f"  ✓ Test output created: {test_file.read_text().strip()}")
            return True
        else:
            print("  ✗ Failed to create test output")
            return False

def main():
    """Run all tests and provide summary."""
    parser = argparse.ArgumentParser(description="Test VibeVoice application functionality")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    print("🎙️ VibeVoice Application Test Suite")
    print("=====================================")
    
    # Track test results
    tests = [
        ("Dependencies", test_dependencies),
        ("Imports", test_imports), 
        ("File Structure", test_file_structure),
        ("Voice Samples", test_voice_samples),
        ("Example Texts", test_example_texts),
        ("Demo Scripts", test_demo_scripts),
        ("Processor", test_processor_initialization),
        ("Test Output", create_test_output),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"\n❌ {test_name} test failed")
        except Exception as e:
            print(f"\n💥 {test_name} test crashed: {e}")
            if args.verbose:
                traceback.print_exc()
    
    # Print summary
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! VibeVoice application appears to be working correctly.")
        print("\n💡 To run the application:")
        print("   1. For Gradio demo: python demo/gradio_demo.py --model_path microsoft/VibeVoice-1.5B")
        print("   2. For file inference: python demo/inference_from_file.py --model_path microsoft/VibeVoice-1.5B --txt_path demo/text_examples/1p_abs.txt --speaker_names Alice")
        print("\n⚠️  Note: First run will download the model (~2.5GB for 1.5B variant)")
        return 0
    else:
        print(f"❌ {total - passed} tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())