
## about repositories and archives

- a repository is where backups are stored, comprising of multiple archives
- an archive is a snapshot of the backed up data at some point in time
- a checkpoint is an incomplete state of an archive, to be able to resume an interrupted backup
- a repository should be used for backing up the same set of directories of a host
    - it's best not to have several source hosts backup to the same repository
    - and not have several users backup their data to the same repository (unless it's an admin having access to all users who performs the backups)

## tip: use env var

- the borg repo path is used by most borg commands
- by setting `$BORG_REPO`, it spares passing it everytime
- for example:

```
export BORG_REPO=ssh://YOUR_BACKUP_HOST/YOUR/BACKUP/PATH
```

## backup the data

```
ARCHIVE_NAME={hostname}-{user}-{now:%Y-%m-%d_%H:%M:%S}
EXCLUDE_FILE=$HOME/exclude-from-backup.borg.conf
borg create \
	--exclude-from "$EXCLUDE_FILE" \
	--exclude-caches \
	--one-file-system \
	--checkpoint-interval 600 \
	--progress \
	--stats \
	--show-rc \
	::"$ARCHIVE_NAME" \
	~
```

### exclude unimportant/transient data from backup

there are 2 mechanisms:

- global exclude config file
- local `CACHEDIR.TAG` files

#### global exclude config file

have an exclude file (`$EXCLUDE_FILE`), containing for example:

```
*/lost+found
*.pyc
*/__pycache__
```

#### local `CACHEDIR.TAG` files

- a [`CACHEDIR.TAG`](https://bford.info/cachedir/) file in a directory means "don't backup this directory"
- basic tool for creating them: [set-cachedir](https://gitlab.com/hydrargyrum/attic/-/blob/master/set-cachedir/set-cachedir)
- sprinkle these files where needed instead of editing global exclude config, for example:
```
set-cachedir ~/.cache
```
- some apps automatically create those files, for example `pytest` in `.pytest_cache/` folders

## trim old backups


```
# trim old backups but keep some granularity, 7 daily backups + 3 monthly backups
borg prune --list \
	-d 7 \
	-m 3

# then save disk space after old backups were trimmed
borg compact --progress --cleanup-commits
```

## basic backup integrity check

**warning:** this only verifies the backup data isn't internally corrupted, it does not replace a true backup restore test to verify all that should have been backed up was indeed backed up

```
borg check --progress --show-rc --repository-only
```

## list backups and data

### list archives

```
borg list
```

### list files in one archive

```
borg list ::YOUR_ARCHIVE_NAME
```


## restore some data

warning: restores data in current directory

```
borg extract --list ::YOUR_ARCHIVE_NAME path/to/some/file
```

this will restore the backed up `path/to/some/file` into `./path/to/some/file`
