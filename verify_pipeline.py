# verify_pipeline.py
import os
import sys
import hashlib
import jax
import jax.numpy as jnp
from bs4 import BeautifulSoup

def test_jax_sciml_compilation():
    print("[TDD] Executing JAX/XLA Compilation Test...")
    b, n, d, k = 4, 10, 8, 3
    key = jax.random.PRNGKey(42)
    mock_tensor = jax.random.normal(key, (b, n, d, k))
    
    @jax.jit
    def target_filter(tensor):
        signal = jnp.mean(tensor, axis=-1)
        return jnp.tanh(signal)
    
    try:
        output = target_filter(mock_tensor)
        assert output.shape == (b, n, d)
        print(f"✅ JAX Test Passed. Compiled Tensor Shape: {output.shape}")
        return True
    except Exception as e:
        print(f"❌ JAX Compilation Failed: {str(e)}")
        return False

def test_html_dom_structure():
    print("[TDD] Analyzing HTML DOM and Asset Integrity...")
    errors = 0
    
    # 1. index.html tarkastus
    if not os.path.exists("index.html"):
        print("❌ Error: index.html not found.")
        return False
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    if not soup.find("section", id="hero"):
        print("❌ Validation Error: index.html: <section id='hero'> puuttuu.")
        errors += 1
    if not soup.find("video", id="hero-video"):
        print("❌ Validation Error: index.html: <video id='hero-video'> puuttuu.")
        errors += 1
    else:
        if not os.path.exists("video1.mp4"):
            print("❌ Asset Error: video1.mp4 puuttuu projektin juuresta!")
            errors += 1
            
    # 2. Services.html tarkastus
    if not os.path.exists("services.html"):
        print("❌ Error: services.html not found.")
        return False
    with open("services.html", "r", encoding="utf-8") as f:
        s_soup = BeautifulSoup(f.read(), "html.parser")
        
    for p_id in ["pipeline-tensor", "pipeline-tqg", "pipeline-fsm"]:
        if not s_soup.find(id=p_id):
            print(f"❌ Validation Error: services.html: Elementtiä id='{p_id}' puuttuu.")
            errors += 1

    if errors == 0:
        print("✅ HTML DOM and Asset Validation Passed.")
        return True
    return False

def generate_build_audit_hash():
    hasher = hashlib.sha256()
    for name in ["index.html", "services.html"]:
        if os.path.exists(name):
            with open(name, "rb") as f:
                hasher.update(f.read())
    build_hash = hasher.hexdigest()
    print(f"[AUDIT] Build SHA256 Signature: {build_hash}")
    return build_hash

if __name__ == "__main__":
    print("="*60)
    print("VOJKER INFRASTRUCTURE SUITE: RUNNING TESTS")
    print("="*60)
    if test_jax_sciml_compilation() and test_html_dom_structure():
        generate_build_audit_hash()
        print("🚀 ALL SYSTEMS NOMINAL - READY FOR DEPLOYMENT")
        sys.exit(0)
    sys.exit(1)