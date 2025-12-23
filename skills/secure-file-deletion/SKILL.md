---
name: secure-file-deletion
description: Securely delete files beyond recovery using overwriting techniques, ensuring data privacy and compliance with data protection regulations
---

# Secure File Deletion Skill

Permanently delete files beyond recovery using secure deletion methods including overwriting, DoD standards, and verification.

## When to Use This Skill

Activate this skill when the user:
- Needs to permanently delete sensitive files
- Wants to ensure data cannot be recovered
- Requires compliance with data protection regulations (GDPR, HIPAA)
- Mentions "secure delete", "shred", "wipe", "permanent deletion"
- Asks about data sanitization
- Needs to decommission storage devices

## Core Capabilities

### 1. Secure Deletion Methods
- **Single Pass**: Overwrite with zeros (fast)
- **DoD 5220.22-M**: 3-pass overwrite (medium security)
- **Gutmann Method**: 35-pass overwrite (maximum security)
- **Random Data**: Overwrite with random bytes
- **Custom Patterns**: User-defined overwrite patterns

### 2. Verification
- Hash verification before/after deletion
- Free space analysis
- Recovery attempt testing
- Deletion confirmation logging

### 3. Batch Operations
- Directory tree deletion
- Pattern-based file selection
- Scheduled secure deletion
- Automated cleanup scripts

## Tools and Commands

### shred (Linux/Mac)
```bash
# Basic secure deletion (3 passes)
shred -vfz -n 3 sensitive_file.txt

# DoD 5220.22-M standard (7 passes)
shred -vfz -n 7 file.pdf

# Gutmann method (35 passes)
shred -vfz -n 35 top_secret.doc

# Delete and remove file
shred -vfzu -n 3 file.txt

# Secure delete entire directory
find /path/to/dir -type f -exec shred -vfzu -n 3 {} \;
```

### srm (Secure Remove)
```bash
# Install srm
sudo apt-get install secure-delete

# Simple deletion (7 passes)
srm file.txt

# Fast deletion (1 pass)
srm -f file.txt

# Recursive directory deletion
srm -r /path/to/directory

# DoD compliant
srm -D file.txt
```

### wipe
```bash
# Wipe file with default passes
wipe file.txt

# Quick wipe (4 passes)
wipe -q file.txt

# Recursive wipe
wipe -r directory/

# Force wipe (no confirmation)
wipe -f file.txt
```

### dd (Low-level overwrite)
```bash
# Overwrite file with zeros
dd if=/dev/zero of=file.txt bs=1M count=10

# Overwrite with random data
dd if=/dev/urandom of=file.txt bs=1M count=10

# Wipe entire disk/partition (BE CAREFUL!)
sudo dd if=/dev/zero of=/dev/sdX bs=1M status=progress
```

### Secure Free Space Wiping
```bash
# Wipe free space on partition
sfill -f /mount/point

# Quick free space wipe
sfill -I /mount/point

# Wipe swap space
sudo swapoff -a
sudo dd if=/dev/zero of=/dev/swap_partition
sudo mkswap /dev/swap_partition
sudo swapon -a
```

## Deletion Standards

### NIST 800-88
- **Clear**: Logical deletion (standard rm)
- **Purge**: Cryptographic erase or overwrite
- **Destroy**: Physical destruction

### DoD 5220.22-M
1. Pass 1: Write 0
2. Pass 2: Write 1
3. Pass 3: Write random character
4. Verify

### Gutmann Method (35 passes)
- 4 random passes
- 27 specific patterns
- 4 random passes
- Maximum security but slow

## Security Levels

| Level | Method | Passes | Speed | Use Case |
|-------|--------|--------|-------|----------|
| Low | Single zero pass | 1 | Fast | Non-sensitive data |
| Medium | DoD 5220.22-M | 3-7 | Medium | Business documents |
| High | Gutmann | 35 | Slow | Top secret data |
| SSD | Trim + Encrypt | N/A | Fast | Solid state drives |

## SSD Considerations

**Problem**: Traditional overwriting doesn't work on SSDs due to wear leveling.

**Solutions**:
```bash
# TRIM (marks blocks for deletion)
sudo fstrim -v /mount/point

# Secure Erase (ATA command)
sudo hdparm --user-master u --security-set-pass password /dev/sdX
sudo hdparm --user-master u --security-erase password /dev/sdX

# Encryption before deletion
cryptsetup luksFormat /dev/sdX
# Then delete encryption key
```

## Python Implementation

```python
import os
import random
import hashlib

class SecureDelete:
    def secure_delete_file(self, filepath, passes=3):
        """Securely delete file with multiple overwrites"""
        file_size = os.path.getsize(filepath)

        with open(filepath, "ba+", buffering=0) as f:
            for pass_num in range(passes):
                f.seek(0)
                if pass_num == 0:
                    # First pass: zeros
                    f.write(b'\x00' * file_size)
                elif pass_num == 1:
                    # Second pass: ones
                    f.write(b'\xFF' * file_size)
                else:
                    # Subsequent passes: random data
                    f.write(os.urandom(file_size))
                f.flush()
                os.fsync(f.fileno())

        # Delete the file
        os.remove(filepath)
        print(f"Securely deleted: {filepath} ({passes} passes)")

    def verify_deletion(self, filepath):
        """Verify file no longer exists"""
        return not os.path.exists(filepath)

    def secure_delete_directory(self, dirpath, passes=3):
        """Recursively secure delete directory"""
        for root, dirs, files in os.walk(dirpath, topdown=False):
            for name in files:
                filepath = os.path.join(root, name)
                self.secure_delete_file(filepath, passes)
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(dirpath)
```

## Best Practices

### Do's
- ✅ Verify deletion completion
- ✅ Use appropriate security level for data sensitivity
- ✅ Log deletion operations for compliance
- ✅ Test on non-critical data first
- ✅ Consider disk type (HDD vs SSD)
- ✅ Wipe free space after file deletion
- ✅ Use encryption as first line of defense

### Don'ts
- ❌ Don't use on SSDs without TRIM support
- ❌ Don't forget to secure delete backup copies
- ❌ Don't skip verification
- ❌ Don't assume one pass is enough for sensitive data
- ❌ Don't forget swap space and temporary files

## Compliance Requirements

### GDPR (Right to Erasure)
- Document deletion processes
- Verify data is unrecoverable
- Maintain deletion logs
- Apply to backups as well

### HIPAA
- Secure media disposal
- Cryptographic wiping for ePHI
- Documented procedures

### PCI DSS
- Secure deletion of cardholder data
- Render data unrecoverable
- Annual policy review

## Output Format

Always provide:
1. **Deletion Method**: Passes, pattern used
2. **Verification**: Confirmation of deletion
3. **Time Taken**: Duration of operation
4. **Files Affected**: Count and size
5. **Compliance**: Standards met
6. **Logs**: Deletion audit trail

## Integration with Other Skills

- **digital-forensics**: Verify data is unrecoverable
- **file-organization**: Automated cleanup of old files
- **data-privacy**: GDPR compliance
- **system-security**: Secure decommissioning

## Resources

- NIST 800-88: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf
- shred manual: https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html
- secure-delete tools: https://github.com/euspectre/sec-delete
