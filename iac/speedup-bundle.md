The command you've provided combines `make` with `bundle install` in a manner that suggests `make` is being used to parallelize the `bundle install` command, which is not correct. The `make -j $(nproc)` syntax is used to specify parallel jobs for `make`, but it doesn't apply to `bundle install`.

To install required gems with Bundler correctly, you should just use the `bundle install` command without `make`. If you're looking to improve the performance of `bundle install`, you can use the `--jobs` (or `-j`) option with Bundler itself to specify the number of gems to install in parallel. Here's how you can do it:

```yaml
- name: Install required gems with Bundler
  ansible.builtin.shell:
    chdir: "{{ project_directory }}"
    cmd: "bundle install --jobs=$(nproc)"
```

This command will run `bundle install` in the specified directory and use Bundler's own mechanism for parallel installation with the number of jobs set to the output of `$(nproc)`, which returns the number of processing units available. This is the correct approach to potentially speeding up gem installations by taking advantage of multiple cores.
